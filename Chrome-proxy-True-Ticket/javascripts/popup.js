// popup.js
// alt + shift + F for fix 

var proxySetting = JSON.parse(localStorage.proxySetting);
var iplist;
var bypasslist = proxySetting['bypasslist'];
var proxyRule = proxySetting['proxy_rule'];
var httpHost = proxySetting['http_host'];
var httpPort = proxySetting['http_port'];
var chinaList = JSON.parse(localStorage.chinaList);
var Malicioussite = '';
var categorysite = '';
var phish = '';
var cache;

var user = '';
var pass = '';



/**
 * set popup page item blue color
 *
 */
function color_proxy_item() {
    var mode, rules, proxyRule;

    chrome.proxy.settings.get({ 'incognito': false },
        function (config) {
            //console.log(JSON.stringify(config));
            mode = config['value']['mode'];
            rules = config['value']['rules'];

            if (rules) {
                if (rules.hasOwnProperty('singleProxy')) {
                    proxyRule = 'singleProxy';
                } else if (rules.hasOwnProperty('proxyForHttp')) {
                    proxyRule = 'proxyForHttp';
                } else if (rules.hasOwnProperty('proxyForHttps')) {
                    proxyRule = 'proxyForHttps'
                } else if (rules.hasOwnProperty('proxyForFtp')) {
                    proxyRule = 'proxyForFtp';
                }

            }
            if (mode == 'system') {
                $('#sys-proxy').addClass('selected');
                document.getElementById("massge_off").hidden = true;
            } else if (mode == 'direct') {
                $('#direct-proxy').addClass('selected');
            } else if (mode == 'pac_script') {
                $('#pac-script').addClass('selected');
            } else if (mode == 'auto_detect' || mode == 'fixed_servers') {
                document.getElementById("massge_off").hidden = false;
                $('#auto-detect').addClass('selected');

            } else {
                scheme = rules[proxyRule]['scheme'];
                $('#http-proxy').addClass('selected');

            }
        });
}

/**
 * set the icon on or off
 *
 */
function iconSet(str) {

    var icon = {
        path: 'images/on.png',
    }
    if (str == 'safe') {
        icon['path'] = 'images/checked.png';
    }
    if (str == 'malicious') {
        icon['path'] = 'images/malicious.png';
    }
    if (str == 'unsafe') {
        icon['path'] = 'images/badsite.png';
    }
    if (str == 'off') {
        icon['path'] = 'images/off.png';
    }
    chrome.browserAction.setIcon(icon);
}



function proxySelected(str) {
    var id = '#' + str;
    $('li').removeClass('selected');
    $(id).addClass('selected');
}




/**
 * set system proxy
 *
 */
function sys_Proxy() {

    var config = {
        mode: 'system',
    };

    chrome.proxy.settings.set(
        { value: config, scope: 'regular' },
        function () { });
    resetUA();
    iconSet('off');
    proxySelected('sys-proxy')
    color_proxy_item();
    chrome.tabs.getSelected(null, function (tab) {
        var code = 'window.location.reload();';
        chrome.tabs.executeScript(tab.id, { code: code });
    });
}





/**
 * set auto detect proxy
 *
 */
function SafeMode() {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        var tab = tabs[0];
        var url = new URL(tab.url)
        var domain = url.hostname;
        var req = new XMLHttpRequest();
        var url = "https://asqwzx1.pythonanywhere.com/".concat("getResult/", domain);
        //document.getElementById('Result-site').innerHTML= url;
        req.open('GET', url, true, user, pass);
        req.onreadystatechange = processResponse;
        req.send(null);
        function processResponse() {
            if (req.readyState == 4 &&
                req.status == 200) {
                var str = JSON.parse(req.responseText);
                if (str.ip && str.UserAgent) {
                    var substring = str.ip.split(':');
                    httpHost = substring[0];
                    httpPort = substring[1];
                    var proxySetting = JSON.parse(localStorage.proxySetting);
                    proxySetting['http_host'] = httpHost;
                    proxySetting['http_port'] = httpPort;
                    var settings = JSON.stringify(proxySetting);
                    localStorage.proxySetting = settings;
                    setUA(str.UserAgent, false);
                    removeAllForFilter();
                    autoProxy()
                    color_proxy_item();
                    chrome.tabs.getSelected(null, function (tab) {
                        var code = 'window.location.reload();';
                        chrome.tabs.executeScript(tab.id, { code: code });
                    });
                }
                else if (str.Trustable == "True") {
                    document.getElementById("massge").innerHTML = "This site is trustable";
                    document.getElementById("massge").style.color = "green";

                }
                else {
                    document.getElementById("massge").innerHTML = "Sorry this site is unsupported now";
                    document.getElementById("massge").style.color = "gray";
                }
            }
        };

    });
}



function autoProxy() {
    var config = {
        mode: "fixed_servers",
        rules: {
            singleProxy: {
                scheme: "http",
                host: httpHost,
                port: parseInt(httpPort)
            },
            bypassList: ["foobar.com", "192.168.1.1/16", "*.foobar.com", "*foobar.com:99", "https://x.*.y.com:99"]
        }
    };
    chrome.proxy.settings.set(
        { value: config, scope: 'regular' },
        function () { });

    iconSet('on');
    proxySelected('auto-detect');
}


chrome.proxy.onProxyError.addListener(function (details) {
    console.log(details.error);
});




function CheckSite() {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        var tab = tabs[0];
        var url = new URL(tab.url);
        var domain = url.hostname
        Malicioussite = '';
        categorysite = '';
        phish = '';
        phishtank(url);
        Malicious(domain.replace("www.", ""));
        category(url);
        while (Malicioussite == '' || categorysite == '' || phish == '');
        if (categorysite != 'false' && Malicioussite != 'true' && phish != 'false') {
            var req = new XMLHttpRequest();
            if (Malicioussite == 'unsafe' || categorysite == 'unsafe' || phish == 'unsafe')
                var url = "https://asqwzx1.pythonanywhere.com/".concat("CheckSite/", domain, "/false");
            else
                var url = "https://asqwzx1.pythonanywhere.com/".concat("CheckSite/", domain, "/true");
            req.open('GET', url, true, user, pass);
            req.onreadystatechange = processResponse;
            req.send(null);
            function processResponse() {
                if (req.readyState == 4 &&
                    req.status == 200) {
                    var str = JSON.parse(req.responseText);
                    if (str.Trustable == "True") {
                        iconSet("safe");
                        document.getElementById("massge").innerHTML = 'This site is safe';
                        document.getElementById("massge").style.color = "green";
                    }
                    else if (str.Trustable == "False" && str.ip) {
                        document.getElementById("massge").innerHTML = 'This site is unsafe'
                        document.getElementById("massge").style.color = "red";
                        iconSet("unsafe");
                    }
                    else {
                        document.getElementById("massge").innerHTML = 'This site is unsupported';
                        document.getElementById("massge").style.color = "gray";
                    }
                }
                //document.getElementById('Result-site').innerHTML=str.Trustable ;
            }
        }
    });

}


function phishtank(url) {
    var req = new XMLHttpRequest();
    var url = "https://checkurl.phishtank.com/checkurl/index.php?url=".concat(url);
    req.open('GET', url, false);
    req.onreadystatechange = processResponse;
    try { req.send(null); }
    catch{ phish = 'unsafe'; }
    function processResponse() {
        if (req.readyState == 4 &&
            req.status == 200) {
            try {
                var xmlDoc = req.responseXML;
                var personIterator = xmlDoc.evaluate('//in_database', xmlDoc, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
                if (personIterator.singleNodeValue.textContent == 'true') {
                    var person = xmlDoc.evaluate('//verified', xmlDoc, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
                    phish = person.singleNodeValue.textContent;
                    if (phish == 'false') {
                        iconSet("malicious");
                        document.getElementById("massge").innerHTML = 'This is a phish site';
                        document.getElementById("massge").style.color = "red";
                        alert("This is a phish site");
                    }
                }

                else
                    phish = 'true';
            }
            catch{ phish = 'unsafe'; }

        }
    };
}

function Malicious(domain) {
    var req = new XMLHttpRequest();
    var url = "https://www.urlvoid.com/scan/".concat(domain);
    req.open('GET', url, false);
    req.onreadystatechange = processResponse;
    try { req.send(null); }
    catch{ Malicioussite = 'unsafe'; }
    function processResponse() {
        if (req.readyState == 4 &&
            req.status == 200) {
            var str = req.responseText;
            if (str.search("label-danger") == -1)
                Malicioussite = "false"
            else {
                Malicioussite = "true"
                iconSet("malicious");
                document.getElementById("massge").innerHTML = 'This is a malicious site';
                document.getElementById("massge").style.color = "red";
                alert("This is a malicious site");
            }
        }

    }
}


function category(url) {
    var req = new XMLHttpRequest();
    var url = "https://fortiguard.com/webfilter?q=".concat(url);
    req.open('GET', url, false);
    req.onreadystatechange = processResponse;
    try { req.send(null); }
    catch{
        var req = new XMLHttpRequest();
        var url = "https://fortiguard.com/search?q=".concat(url, "&engine=1");
        req.open('GET', url, false);
        req.onreadystatechange = processResponse;
        try { req.send(null); }
        catch{ categorysite = 'unsafe'; }
    }
    function processResponse() {
        if (req.readyState == 4 &&
            req.status == 200) {
            var str = req.responseText;
            if (Malicioussite == "false" || phish == 'true') {
                if (str.search("Travel") == -1) {
                    categorysite = "false"
                    document.getElementById("massge").innerHTML = "Sorry we work only with travel sites ";
                    document.getElementById("massge").style.color = "blue"
                }
                else {
                    categorysite = "true"
                }
            }
            else
                categorysite = "dont care"
        }

    }
}



//// user agent set and reset
function setUA(ua, flag = true) {
    chrome.runtime.sendMessage({
        type: 'setUA',
        ua: ua
    });
    if (flag)
        window.close();
}


function resetUA() {
    chrome.runtime.sendMessage({
        type: 'resetUA'
    });
}


///////////////////////////////////////coockis

// Compares cookies for "key" (name, domain, etc.) equality, but not "value"
// equality.
function cookieMatch(c1, c2) {
    return (c1.name == c2.name) && (c1.domain == c2.domain) &&
        (c1.hostOnly == c2.hostOnly) && (c1.path == c2.path) &&
        (c1.secure == c2.secure) && (c1.httpOnly == c2.httpOnly) &&
        (c1.session == c2.session) && (c1.storeId == c2.storeId);
}

// Returns an array of sorted keys from an associative array.
function sortedKeys(array) {
    var keys = [];
    for (var i in array) {
        keys.push(i);
    }
    keys.sort();
    return keys;
}

// Shorthand for document.querySelector.
function select(selector) {
    return document.querySelector(selector);
}

function CookieCache() {
    this.cookies_ = {};

    this.reset = function () {
        this.cookies_ = {};
    }

    this.add = function (cookie) {
        var domain = cookie.domain;
        if (!this.cookies_[domain]) {
            this.cookies_[domain] = [];
        }
        this.cookies_[domain].push(cookie);
    };

    this.remove = function (cookie) {
        var domain = cookie.domain;
        if (this.cookies_[domain]) {
            var i = 0;
            while (i < this.cookies_[domain].length) {
                if (cookieMatch(this.cookies_[domain][i], cookie)) {
                    this.cookies_[domain].splice(i, 1);
                } else {
                    i++;
                }
            }
            if (this.cookies_[domain].length == 0) {
                delete this.cookies_[domain];
            }
        }
    };


    // Returns a sorted list of cookie domains that match |filter|. If |filter| is
    //  null, returns all domains.
    this.getDomains = function (filter) {
        var result = [];
        sortedKeys(this.cookies_).forEach(function (domain) {
            if (!filter || domain.indexOf(filter) != -1) {
                result.push(domain);
            }
        });
        return result;
    }

    this.getCookies = function (domain) {
        return this.cookies_[domain];
    };
}

function removeAllForFilter() {
    var cache = new CookieCache();
    chrome.cookies.getAll({}, function (cookies) {
        for (var i in cookies) {
            cache.add(cookies[i]);
        }
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            var tab = tabs[0];
            var url = new URL(tab.url);
            var host = url.hostname.replace("www.", "");
            cache.getDomains(host).forEach(function (domain) {
                cache.getCookies(domain).forEach(function (cookie) {
                    removeCookie(cookie);
                });
            });
        });
    });
}


function removeCookie(cookie) {
    var url = "http" + (cookie.secure ? "s" : "") + "://" + cookie.domain +
        cookie.path;
    chrome.cookies.remove({ "url": url, "name": cookie.name });
}



//////////////////////////

document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('#CheckSite').addEventListener('click', CheckSite);
    document.querySelector('#sys-proxy').addEventListener('click', sys_Proxy);
    document.querySelector('#auto-detect').addEventListener('click', SafeMode);

    $('[data-i18n-content]').each(function () {
        var message = chrome.i18n.getMessage(this.getAttribute('data-i18n-content'));
        if (message)
            $(this).html(message);
    });


});




$(document).ready(function () {
    color_proxy_item();
    user = (chrome.extension.getBackgroundPage().user);
    pass = (chrome.extension.getBackgroundPage().pass);
});



