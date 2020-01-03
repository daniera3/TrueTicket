var MYkey;
var user='';
var pass='';

function LoadUrlList() {
    user=(chrome.extension.getBackgroundPage().user);
    pass=(chrome.extension.getBackgroundPage().pass);
    const Url = 'https://asqwzx1.pythonanywhere.com/GetURL';
    var req = new XMLHttpRequest();
    req.open('GET', Url, false,user, pass);
    req.onreadystatechange = processResponse;
    req.send(null);
    function processResponse() {
        if (req.readyState == 4 &&
            req.status == 200) {
            var json_Req = JSON.parse(req.responseText);
            window.onload = function () {
                if (json_Req['data'].length > 0) {
                    json_Req['data'].forEach(function (obj) {
                        var Select = document.getElementById('URL_LIST');
                        var option = document.createElement("option");
                        option.text = obj['HostName'];
                        option.value = obj['HostName'];
                        Select.appendChild(option);

                    });
                }
            };
        };
    };


}

function myreload() {
    document.getElementById("body").hidden = false;
    document.getElementById("div_password").hidden = true;
    document.getElementById("btPassword2").hidden = false;
    document.getElementById("btPassword").hidden = true;
    document.getElementById("Xpath_input").value = '';
    document.getElementById("FullURL_input").value = '';
    document.getElementById("myPass").value = '';
    document.getElementById("FullURL_input").disabled = false;
    document.getElementById("selected_item").innerHTML='';
    var Select = document.getElementById('URL_LIST');
    while (Select.length > 0) {
        Select.remove(0);
    }
    const Url = 'https://asqwzx1.pythonanywhere.com/GetURL';
    var req = new XMLHttpRequest();
    req.open('GET', Url, false,user, pass);

    req.onreadystatechange = processResponse;
    req.send(null);
    function processResponse() {
        if (req.readyState == 4 &&
            req.status == 200) {
            var json_Req = JSON.parse(req.responseText);
            if (json_Req['data'].length > 0) {
                json_Req['data'].forEach(function (obj) {
                    var Select = document.getElementById('URL_LIST');
                    var option = document.createElement("option");
                    option.text = obj['HostName'];
                    option.value = obj['HostName'];
                    Select.appendChild(option);

                });
            }

        };
    };
}

function accept_password() {
    var password = document.getElementById("myPass").value;
    if (password != null && password != '') {
        const json = JSON.stringify({ "password": password });
        const Url = 'https://asqwzx1.pythonanywhere.com/accept';
        var req = new XMLHttpRequest();
        req.open('POST', Url, false,user, pass);
        req.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        req.onreadystatechange = processResponse;
        req.send(json);
        function processResponse() {
            if (req.readyState == 4 &&
                req.status == 200) {
                var json_Req = JSON.parse(req.responseText);
                if (json_Req['msg'] == "accept") {
                    MYkey=password;
                    document.getElementById("body").hidden = false;
                    document.getElementById("div_password").hidden = true;
                    document.getElementById("btPassword2").hidden = false;
                    document.getElementById("btPassword").hidden = true;

                    document.getElementById("myPass").value = '';

                }
                else
                    window.close();
            };
        };
    }
    else
        window.close();
}

function delet_url () {
    var HostName = document.getElementById("selected_item").innerHTML;
    var FullName = document.getElementById("FullURL_input").value;
    var password = document.getElementById("myPass").value;

    if (password != null && password != '') {
        const json = JSON.stringify({ "password": password });
        const Url = 'https://asqwzx1.pythonanywhere.com/accept';
        var req = new XMLHttpRequest();
        req.open('POST', Url, false,user, pass);
        req.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        req.onreadystatechange = processResponse;
        req.send(json);
        function processResponse() {
            if (req.readyState == 4 &&
                req.status == 200) {
                var json2_Req = JSON.parse(req.responseText);
                if (json2_Req['msg'] == "accept") {
                    document.getElementById("myPass").value = '';
                    const json2 = JSON.stringify({ "HostName": HostName,"pass":MYkey  });
                    if (HostName != '' && FullName != '' && FullName != "ERROR") {
                        const Url = 'https://asqwzx1.pythonanywhere.com/DelURL';
                        var req2 = new XMLHttpRequest();
                        req2.open('POST', Url, false,user, pass);
                        req2.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
                        req2.onreadystatechange = processResponses;
                        req2.send(json2);
                        function processResponses() {
                            if (req.readyState == 4 &&
                                req.status == 200) {
                                var json_Req3 = JSON.parse(req2.responseText);
                                alert(json_Req3['msg']);
                                //location.reload(true);
                                myreload();

                            };
                        };
                    }

                }
                else
                    alert("bad password");
            };
        };
    }
    else {
        alert("insert password");
    }
}


$('document').ready(function () {
    var buttonPassword = document.getElementById("btPassword");
    var btPassword = document.getElementById("btPassword2");
    
    buttonPassword.onclick = function () { accept_password(); };
    document.querySelector('#myPass').addEventListener('keypress', function (e) {
        var key = e.which || e.keyCode;
        if (key === 13) { // 13 is enter
            if (btPassword.hidden)
            accept_password();
            else
            delet_url();
        }
    });


    var selObj = document.getElementById("URL_LIST");
    var buttonObj = document.getElementById("setXpath");
    var buttonObj_del = document.getElementById("deleteURL");
    selObj.onchange = function () {
        document.getElementById("select_label").hidden = false;
        var selValue = selObj.options[selObj.selectedIndex].text;
        document.getElementById("selected_item").innerHTML = selValue;
        const json = JSON.stringify({ "HostName": selValue });
        const Url = 'https://asqwzx1.pythonanywhere.com/GetFullURL';
        var req = new XMLHttpRequest();
        req.open('POST', Url, false,user, pass);
        req.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        req.onreadystatechange = processResponse;
        req.send(json);
        function processResponse() {
            if (req.readyState == 4 &&
                req.status == 200) {
                var json_Req = JSON.parse(req.responseText);
                if (json_Req['data'] != "") {
                    document.getElementById("FullURL_input").value = json_Req['data'];
                    document.getElementById("FullURL_input").disabled = true;
                }
                else {
                    document.getElementById("FullURL_input").value = '';
                    document.getElementById("FullURL_input").disabled = false;
                }


            };
        };

    };
    buttonObj.onclick = function () {
        var HostName = document.getElementById("selected_item").innerHTML;
        var Xpath = document.getElementById("Xpath_input").value;
        var FullName = document.getElementById("FullURL_input").value;
        const json = JSON.stringify({ "HostName": HostName, "Xpath": Xpath, "FullName": FullName,"pass":MYkey });
        if (HostName != '' && Xpath != '' && FullName != '' && FullName != "ERROR") {
            const Url = 'https://asqwzx1.pythonanywhere.com/setXpath';
            var req = new XMLHttpRequest();
            req.open('POST', Url, false,user, pass);
            req.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
            req.onreadystatechange = processResponse;
            req.send(json);
            function processResponse() {
                if (req.readyState == 4 &&
                    req.status == 200) {
                    var json_Req = JSON.parse(req.responseText);
                    alert(json_Req['msg']);
                    myreload();
                    //location.reload(true);


                };
            };
        }
        else {
            alert("One or more of the fields are missing");
        }
    }
    buttonObj_del.onclick = function() {
        var HostName = document.getElementById("selected_item").innerHTML;
        var FullName = document.getElementById("FullURL_input").value;
        var flag = document.getElementById("FullURL_input").disabled;
        if (HostName != '' && FullName != '' && FullName != "ERROR" && flag) {
            document.getElementById("lbPassword").innerHTML = "Please enter your password \n for delete url for " + HostName;
            document.getElementById("body").hidden = true;
            document.getElementById("div_password").hidden = false;
            btPassword.onclick =  function() {delet_url();};
        }
        else {
            alert("One or more of the fields are missing");
        }
    }
});


LoadUrlList()