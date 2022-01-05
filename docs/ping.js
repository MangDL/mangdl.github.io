function req(key) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", `https://kv.whi-ne.workers.dev?key=${key}`, false);
    xhr.send(null);
    return xhr.response;
}

var all = JSON.parse(req("all"));

window.onload = function () {
    var modal = document.getElementById("myModal");
    var span = document.getElementById("close");
    span.onclick = function () {
        modal.style.display = "none";
    }
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
    var modp = document.getElementById("mod-p");

    stat_boc = function () {
        while (modp.firstChild) {
            modp.removeChild(modp.firstChild);
        }

        var h3 = document.createElement("h3");
        h3.append("STATUS:");
        var stat = "";
        if (this.getAttribute("stat") === "true") {
            stat = "Working";
        } else {
            stat = "Failing";
        }
        modp.append(h3, stat);

        var h3 = document.createElement("h3");
        h3.append("ONLINE:");
        var stat = "";
        if (this.getAttribute("ol") === "true") {
            stat = "True";
        } else {
            stat = "False";
        }
        modp.append(h3, stat);

        var h3 = document.createElement("h3");
        h3.append("PING:");
        modp.append(h3, `${this.getAttribute("ping")} ms`);

        var h3 = document.createElement("h3");
        h3.append("TEST:");
        if (this.getAttribute("test") === "true") {
            test = "Working";
        } else {
            test = "Failing";
        }
        modp.append(h3, test);

        if (this.getAttribute("notes")) {
            var h3 = document.createElement("h3");
            h3.append("NOTES:")
            modp.append(h3, this.getAttribute("notes"))
        }

        modal.style.display = "block";
    };

    ol_boc = function () {
        while (modp.firstChild) {
            modp.removeChild(modp.firstChild);
        }

        var h3 = document.createElement("h3");
        h3.append("ONLINE:");
        var stat = "";
        if (this.getAttribute("ol") === "true") {
            stat = "True";
        } else {
            stat = "False";
        }
        modp.append(h3, stat);

        var h3 = document.createElement("h3");
        h3.append("PING:");
        modp.append(h3, `${this.getAttribute("ping")} ms`);

        if (this.getAttribute("notes")) {
            var h3 = document.createElement("h3");
            h3.append("NOTES:")
            modp.append(h3, this.getAttribute("notes"))
        }

        modal.style.display = "block";
    };

    test_boc = function () {
        while (modp.firstChild) {
            modp.removeChild(modp.firstChild);
        }

        var h3 = document.createElement("h3");
        h3.append("TEST:");
        if (this.getAttribute("test") === "true") {
            test = "Working";
        } else {
            test = "Failing";
        }
        modp.append(h3, test);

        if (this.getAttribute("notes")) {
            var h3 = document.createElement("h3");
            h3.append("NOTES:")
            modp.append(h3, this.getAttribute("notes"))
        }

        modal.style.display = "block";
    };

    var table = document.getElementById("providers");

    $.each(all, function (k, item) {
        var tr = document.createElement("tr");

        // status
        var stat = document.createElement("td");
        var btn = document.createElement("btn");
        var img = document.createElement("img");
        btn.onclick = stat_boc;
        if (item["stat"] === true) {
            img.src = "https://img.icons8.com/color/48/000000/ok--v1.png";
        } else {
            img.src = "https://img.icons8.com/color/48/000000/cancel--v1.png";
        }
        btn.setAttribute("stat", item["stat"] === true);
        btn.setAttribute("ol", item["ol"] === true);
        btn.setAttribute("ping", parseInt(item["ping"]));
        btn.setAttribute("notes", item["notes"]);
        btn.append(img);
        stat.append(btn);
        tr.append(stat);

        // online
        var stat = document.createElement("td");
        var btn = document.createElement("btn");
        var img = document.createElement("img");
        btn.onclick = ol_boc;
        if (item["ol"] === true) {
            img.src = "https://img.icons8.com/color/48/000000/ok--v1.png";
        } else {
            img.src = "https://img.icons8.com/color/48/000000/cancel--v1.png";
        }
        btn.setAttribute("ol", item["ol"] === true);
        btn.setAttribute("ping", parseInt(item["ping"]));
        btn.setAttribute("notes", item["notes"]);
        btn.append(img);
        stat.append(btn);
        tr.append(stat);

        // test
        var stat = document.createElement("td");
        var btn = document.createElement("btn");
        var img = document.createElement("img");
        btn.onclick = test_boc;
        if (item["test"] === true) {
            img.src = "https://img.icons8.com/color/48/000000/ok--v1.png";
        } else {
            img.src = "https://img.icons8.com/color/48/000000/cancel--v1.png";
        }
        btn.setAttribute("ol", item["ol"] === true);
        btn.setAttribute("ping", parseInt(item["avg"]));
        btn.setAttribute("notes", item["notes"]);
        btn.append(img);
        stat.append(btn);
        tr.append(stat);

        // provider
        var name = document.createElement("td");
        var na = document.createElement("a");
        na.setAttribute("target", "_blank");
        na.setAttribute("href", item["url"]);
        na.textContent = k;
        name.append(na);
        tr.append(name);

        // platform
        var pf = document.createElement("td");
        var p = document.createElement("p");
        p.textContent = item["pf"];
        pf.append(p);
        tr.append(pf);

        // flags
        var flags = ["cf"]
        var i_flag = item["flag"]
        flags.forEach((v) => {
            var flag = document.createElement("td");
            var img = document.createElement("img");
            btn.onclick = test_boc;
            if (i_flag.includes(v)) {
                img.src = "https://img.icons8.com/color/48/000000/ok--v1.png";
            } else {
                img.src = "https://img.icons8.com/color/48/000000/cancel--v1.png";
            }
            flag.append(img);
            tr.append(flag);
        });

        table.append(tr);
    });
}