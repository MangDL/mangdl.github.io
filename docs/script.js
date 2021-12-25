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

function createCopyButton(highlightDiv) {
    const button = document.createElement("button");
    button.className = "copy-code-button";
    button.type = "button";
    button.innerText = "Copy";
    button.addEventListener("click", () =>
        copyCodeToClipboard(button, highlightDiv)
    );
    addCopyButtonToDom(button, highlightDiv);
}

async function copyCodeToClipboard(button, highlightDiv) {
    const codeToCopy = highlightDiv.querySelector(":last-child > pre > code")
        .innerText;
    try {
        result = await navigator.permissions.query({ name: "clipboard-write" });
        if (result.state == "granted" || result.state == "prompt") {
            await navigator.clipboard.writeText(codeToCopy);
        } else {
            copyCodeBlockExecCommand(codeToCopy, highlightDiv);
        }
    } catch (_) {
        copyCodeBlockExecCommand(codeToCopy, highlightDiv);
    } finally {
        codeWasCopied(button);
    }
}

function copyCodeBlockExecCommand(codeToCopy, highlightDiv) {
    const textArea = document.createElement("textArea");
    textArea.contentEditable = "true";
    textArea.readOnly = "false";
    textArea.className = "copyable-text-area";
    textArea.value = codeToCopy;
    highlightDiv.insertBefore(textArea, highlightDiv.firstChild);
    const range = document.createRange();
    range.selectNodeContents(textArea);
    const sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(range);
    textArea.setSelectionRange(0, 999999);
    document.execCommand("copy");
    highlightDiv.removeChild(textArea);
}

function codeWasCopied(button) {
    button.blur();
    button.innerText = "Copied!";
    setTimeout(function () {
        button.innerText = "Copy";
    }, 2000);
}

function addCopyButtonToDom(button, highlightDiv) {
    highlightDiv.insertBefore(button, highlightDiv.firstChild);
    const wrapper = document.createElement("div");
    wrapper.className = "highlight-wrapper";
    highlightDiv.parentNode.insertBefore(wrapper, highlightDiv);
    wrapper.appendChild(highlightDiv);
}

document
    .querySelectorAll(".highlight")
    .forEach((highlightDiv) => createCopyButton(highlightDiv));

function on() {
    document.getElementById("overlay").style.display = "grid";
}

function off() {
    document.getElementById("overlay").style.display = "none";
}

function enlarge(item) {
    on();
    document.getElementById("ol-img").src = item.src;
}

function addEnlarge(enlargeDiv) {
    enlargeDiv.setAttribute("title", "Click me to enlarge!")
}

for (var i of document.querySelectorAll("ul li img")) {
    i.setAttribute("onclick", "enlarge(this)");
}

document
    .querySelectorAll(".el-img")
    .forEach((enlargeDiv) => addEnlarge(enlargeDiv));