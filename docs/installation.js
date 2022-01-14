var items = {
    "Installable": {
        "Windows": { '': [] },
        "MacOS": { '': [] },
        "Linux": { "Distro": ["Debian", "Arch"] }
    },
    "Portable": {
        "Windows": { '': [] },
        "Linux": { "Distro": ["Debian", "Arch"] }
    },
    "Programmatic": {
        "Windows": { "": [] },
        "MacOS": { '': [] },
        "Linux": { "Distro": ["Debian", "Arch"] }
    },
}
window.onload = function () {
    var firstSel = document.getElementById("first");
    var secSel = document.getElementById("second");
    var thirdSel = document.getElementById("third");
    var ts = document.getElementById("ss");
    var ts = document.getElementById("ts");
    var rel = $("#rel")
    for (var x in items) {
        firstSel.options[firstSel.options.length] = new Option(x, x);
    }
    rel.load('./installation/index.html');
    firstSel.onchange = function () {
        rel.empty()
        if (firstSel.value == "") {
            rel.load('./installation/index.html');
            secSel.style = "display: none;";
            ss.style = "display: none;";
            thirdSel.style = "display: none;";
            ts.style = "display: none;";
        } else {
            rel.load(`./installation/OS.html`);
            ss.style = "display: block;";
            secSel.style = "display: block;"
            thirdSel.length = 1;
            secSel.length = 1;
            for (var y in items[this.value]) {
                secSel.options[secSel.options.length] = new Option(y, y);
            }
        }
        if (secSel.value == "") {
            thirdSel.style = "display: none;";
            ts.style = "display: none;";
        }
    }
    secSel.onchange = function () {
        rel.empty()
        var z = Object.values(items[firstSel.value][this.value])[0];
        if (!z.length) {
            thirdSel.style = "display: none;";
            ts.style = "display: none;";
            rel.load(`./installation/${this.value}/${firstSel.value}.html`);
        } else {
            rel.load(`./installation/${secSel.value}/index.html`);
            ts.textContent = Object.keys(items[firstSel.value][this.value])[0];
            ts.style = "display: block;"
            thirdSel.style = "display: block;"
            thirdSel.length = 1;
            for (var i = 0; i < z.length; i++) {
                thirdSel.options[thirdSel.options.length] = new Option(z[i], z[i]);
            }
        }
    }
    thirdSel.onchange = function () {
        rel.empty()
        rel.load(`./installation/${secSel.value}/${firstSel.value}/${thirdSel.value}.html`);
    }
}