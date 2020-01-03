// alt + shift + F for fix 

function loadProxyData() {

    $(document).ready(function () {

        var proxySetting = JSON.parse(localStorage.proxySetting);

        $('#http-host').val(proxySetting['http_host'] || "");
        $('#http-port').val(proxySetting['http_port'] || "");
        $('#bypasslist').val(proxySetting['bypasslist'] || "");
        $('#rules-mode').val(proxySetting['rules_mode'] || "Whitelist");
        $('#proxy-rule').val(proxySetting['proxy_rule'] || "singleProxy");

        if (proxySetting['internal'] == 'china') {
            $('#use-china-list').attr('checked', true);
        }
        $('#bypasslist').prop('disabled', false);
        $('#proxylist').prop('disabled', true);
        $('#china-list').prop('disabled', false);
        $('#blacklist').hide();
        $('#whitelist').show();


    });

}


/**
 * load old proxy info
 */
function loadOldInfo() {
    var mode, url, rules, proxyRule;
    var type, host, port;
    var ret, pacType, pacScriptUrl;

    chrome.proxy.settings.get({ 'incognito': false },
        function (config) {

            mode = config["value"]["mode"];
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

                $('#proxy-rule').val(proxyRule);
            }

            if (mode == "direct" ||
                mode == "system" ||
                mode == "auto_detect") {

                return;

            } else if (mode == "fixed_servers") {

                // we are in manual mode
                type = rules[proxyRule]['scheme'];
                host = rules[proxyRule]['host'];
                port = rules[proxyRule]['port'];
                bypassList = rules.bypassList;

                if (type == 'http') {
                    $('#http-host').val(host);
                    $('#http-port').val(port);
                }

                if (bypassList)
                    $('#bypasslist').val(bypassList.join(','));
            }
        });

    localStorage.firstime = 1;
}

/**
 * get chrome browser proxy settings 
 * and display on the options page
 *
 */
function getProxyInfo(callback) {

    var proxyInfo;
    var proxySetting = JSON.parse(localStorage.proxySetting);
    var mode, rules, proxyRule;

    chrome.proxy.settings.get({ 'incognito': false },
        function (config) {
            // console.log(JSON.stringify(config));
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

            if (mode == 'direct' ||
                mode == 'system' ||
                mode == 'auto_detect') {
                proxyInfo = mode;
            } else if (mode == 'fixed_servers')
                proxyInfo = rules[proxyRule]['scheme'];

            localStorage.proxyInfo = proxyInfo;
            callback(proxyInfo);
        });
}

/**
 * get uniq array
 *
 */
function uniqueArray(arr) {
    var hash = {}, result = [];
    for (var i = 0, l = arr.length; i < l; ++i) {
        if (!hash.hasOwnProperty(arr[i])) {
            hash[arr[i]] = true;
            result.push(arr[i]);
        }
    }
    return result;
}

/**
 * @brief use proxy info to set proxy
 *
 */
function reloadProxy() {

    var type, auto, arrayString;
    var proxy = { type: '', host: '', port: '' };
    var config = {
        mode: '',
        pacScript: {},
        rules: {}
    };

    var proxySetting = JSON.parse(localStorage.proxySetting);

    getProxyInfo(function (info) {

        if (typeof info === 'undefined' ||
            info == 'direct' || info == 'system') {
            return;
        }





        proxy.type = 'http';
        proxy.host = proxySetting['http_host'];
        proxy.port = parseInt(proxySetting['http_port']);

        var rule = proxySetting['proxy_rule'];
        var chinaList = JSON.parse(localStorage.chinaList);
        var bypasslist = proxySetting['bypasslist'];

        if (proxySetting['internal'] == 'china') {
            bypasslist = chinaList.concat(bypasslist.split(','));
        } else {
            bypasslist =
                bypasslist ? bypasslist.split(',') : ['<local>'];
        }

        config.mode = "fixed_servers";
        config.rules.bypassList = uniqueArray(bypasslist);
        config["rules"][rule] = {
            scheme: proxy.type,
            host: proxy.host,
            port: parseInt(proxy.port)
        };


        chrome.proxy.settings.set({
            value: config,
            scope: 'regular'
        }, function () { })
    });

}

/**
 * set system proxy
 *
 */
function sysProxy() {

    var config = {
        mode: "system",
    };
    var icon = {
        path: "images/off.png",
    }

    chrome.proxy.settings.set(
        { value: config, scope: 'regular' },
        function () { });

    chrome.browserAction.setIcon(icon);
}

/**
 * button id save click handler
 *
 */
function save() {

    var proxySetting = JSON.parse(localStorage.proxySetting);
    proxySetting['http_host'] = $('#http-host').val() || "";
    proxySetting['http_port'] = $('#http-port').val() || "";
    proxySetting['bypasslist'] = $('#bypasslist').val() || "";
    proxySetting['proxy_rule'] = $('#proxy-rule').val() || "";
    proxySetting['rules_mode'] = $('#rules-mode').val() || "";

    if ($('#use-china-list').is(':checked')) {
        proxySetting['internal'] = "china";
    }
    else {
        proxySetting['internal'] = "";
    }

    var settings = JSON.stringify(proxySetting);
    //console.log(settings);

    localStorage.proxySetting = settings;
    reloadProxy();
    loadProxyData();

    // sync settings to google cloud
    chrome.storage.sync.set({ 'proxySetting': settings }, function () { });
}


/**
 * set proxy for get pac data
 *
 */
function setPacProxy() {

    var proxy = { type: '', host: '', port: '' };

    pacProxyHost = $('#pac-proxy-host').val().split(':');
    pacViaProxy = $('#pac-via-proxy').val().split(':');

    proxy.type = pacViaProxy[0];
    proxy.host = pacProxyHost[0];
    proxy.port = parseInt(pacProxyHost[1]);

    var config = {
        mode: "fixed_servers",
        rules: {
            singleProxy: {
                scheme: proxy.type,
                host: proxy.host,
                port: proxy.port
            }
        }
    };

    chrome.proxy.settings.set(
        { value: config, scope: 'regular' }, function () { });

}



document.addEventListener('DOMContentLoaded', function () {


    /**  $('#diagnosis').click(function () {
         chrome.tabs.create({ url: 'chrome://net-internals/#proxy' });
     });
     */
    $('input').change(function () { save(); });
});




if (!localStorage.firstime)
    loadOldInfo();
else
    loadProxyData();

getProxyInfo(function (info) { });
