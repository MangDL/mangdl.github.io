<!-- Repository Name. Preferrably 1-5 words long. -->
<h1 align="center" style="font-weight: bold">
    ${title}
</h1>



<!-- Description. Preferrably 1 sentence long. -->
<h3 align="center" style="font-weight: bold">
    WIP: Manga Downloader
</h3>

<p align="center">
	<a href="https://github.com/${organization}/${repo_name}/blob/master/LICENSE.md">
        <img src="https://img.shields.io/badge/LICENSE-A31F34?style=flat-square&logoWidth=25&logo=data:image/png;base64,${license_b64}">
    </a>
    <a href="https://github.com/${organization}/${repo_name}/issues">
        <img src="https://img.shields.io/github/issues/${organization}/${repo_name}.svg?style=flat-square&logo=data:image/png;base64,${issues_b64}">
    </a>
    <a href="https://github.com/${organization}/${repo_name}/network/members">
        <img src="https://img.shields.io/github/forks/${organization}/${repo_name}.svg?style=flat-square&logo=data:image/png;base64,${forks_b64}">
    </a>
    <a href="https://github.com/${organization}/${repo_name}/network/members">
        <img src="https://img.shields.io/github/stars/${organization}/${repo_name}.svg?style=flat-square&logo=data:image/png;base64,${stars_b64}">
    </a>
    <a href="https://github.com/${organization}/${repo_name}/graphs/contributors">
        <img src="https://img.shields.io/github/contributors/${organization}/${repo_name}.svg?style=flat-square&logo=data:image/png;base64,${contributors_b64}">
    </a>
    <a target="_blank" href="https://discord.com/invite/${dc_inv}">
        <img src="https://img.shields.io/discord/${dc_serv}.svg?style=flat-square&logo=data:image/png;base64,${discord_b64}">
    </a>
</p>

<!-- About section. Preferrably 2-5 sentences long. -->
---

<h4 align="center">
The most inefficient manga downloader for PC (and soon, also a reader)
</h4>

---

Github: [github.com/${organization}/${repo_name}](https://github.com/${organization}/${repo_name})

Website: [mangdl.github.io](https://mangdl.github.io)

## **Important**

This project is a work in progress. A package will be released soon as a beta.

To be updated, be sure to watch this repository and join the [Discord Support Server](${dc_inv}) for mangDL.

For the terms of usage and legals, visit [LICENSE.md](LICENSE.md) and [TERMS OF USAGE & DISCLAIMER.md](TERMS%20OF%20USAGE%20%26%20DISCLAIMER.md).

## **Features**

- Ad free
- Batch downloading
- 0% tracking and analytics
- Can be used as a library

### Supported OSes

- Windows
- MacOS
- Linux
- Android

<details>
    <summary><sub>NOTES</sub></summary>
    <sub>
        <i>
            At the moment of writing, there is a fatal error that does not allow this project to run at Termux. Right now, it is being fixed.
            To be updated in the latest commits, be sure to watch this repository.
        </i>
    </sub>
</details>

## **Sites**

- [mangadex.org](https://mangadex.org)
- [manganato.com](https://manganato.com)
- [flamescans.org](https://flamescans.org)

### Coming soon™

- [mangarock.to](https://mangarock.to)

<!-- TOC section. Update when adding sections and subsections fitted in TOC. -->
## **Table of Contents**

- [**Important**](#important)
- [**Features**](#features)
- [**Sites**](#sites)
- [**Table of Contents**](#table-of-contents)
- [**Usage**](#usage)
- [**Getting Started**](#getting-started)
    - [**Prerequisites**](#prerequisites)
    - [**Setup**](#setup)
- [**TODO**](#todo)
- [**Contributions**](#contributions)
- [**Known Issues and Limitations**](#known-issues-and-limitations)
- [**Future of this project**](#future-of-this-project)
- [**License**](#license)
- [**Credits**](#credits)

<!-- Mention examples of application of this repository. -->
## **Usage**

Before using this project, it is recommended to visit [LICENSE.md](LICENSE.md) and [TERMS OF USAGE & DISCLAIMER.md](TERMS%20OF%20USAGE%20%26%20DISCLAIMER.md) for the terms of usage and legals.

```bash
mangdl -h
```

Downloading:

```bash
mangdl dl <title> [OPTIONS]
```

For programmatic use, visit the documentation: [whinee.github.io/mangDL/docs](https://whinee.github.io/mangDL/docs)

## **Getting Started**

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### **Prerequisites**

The following are the required programs and/or packages to run this project:

- For all operating systems:
    - Python 3.6 and higher
        <details>
        <summary>To check that you have Python 3.6 and higher installed, in your preferred terminal, run the following command:</summary>

        ```bash
        python3 --version
        ```

        </details>

    - pip (Package Installer for Python)
        <details>
        <summary>To check that you have pip installed, in your preferred terminal, run the following command:</summary>

        ```bash
        pip3 --version
        ```

        </details>

    - git
        <details>
        <summary>To check that you have git installed, in your preferred terminal, run the following command:</summary>

        ```bash
        git --version
        ```

        </details>

    ![uni](assets/images/prereq_uni.png)

- For windows:
    - [Chocolatey](https://chocolatey.org)
        <details>
        <summary>To check that you have Chocolatey installed, in your preferred terminal, run the following command:</summary>

        ```bash
        choco --version
        ```

        </details>

    - [7zip](https://7-zip.org)
        <details>
        <summary>To check that you have 7zip installed, in your preferred terminal, run the following command:</summary>

        ```bash
        7z --version
        ```

        </details>

    <details>
    <summary>You should get a similar output like the following image:</summary>
    <img src="assets/images/prereq_1.png" alt="1">
    </details>

- For [macOS](https://www.apple.com/mac/):
    - [Homebrew](https://brew.sh)
        <details>
        <summary>To check that you have Homebrew installed, in your preferred terminal, run the following command:</summary>

        ```bash
        brew --version
        ```

        </details>

    - [p7zip](https://github.com/jinfeihan57/p7zip)
        <details>
        <summary>To check that you have p7zip installed, in your preferred terminal, run the following command:</summary>

        ```bash
        7z --version
        ```

        </details>

    <details>
    <summary>You should get a similar output like the following image:</summary>
    <img src="assets/images/prereq_2.png" alt="2">
    </details>

- For [Linux](https://www.linux.org/)
    - [p7zip](https://github.com/jinfeihan57/p7zip)
        <details>
        <summary>To check that you have p7zip installed, in your preferred terminal, run the following command:</summary>

        ```bash
        7z --version
        ```

        </details>

    <details>
    <summary>You should get a similar output like the following image:</summary>
    <img src="assets/images/prereq_3.png" alt="3">
    </details>

If any or all of the above is not installed, follow [this link](INSTALLATION.md):

After checking or installing Python, pip, and git in your machine, proceed to the [setup](#setup) section.

### **Setup**

- Open your preferred console or terminal

- Create a virtual environment using the following command:

    ```bash
    python3 -m venv venv
    ```

- Enter the virtual environment
    - For [Windows 7 and up](https://www.microsoft.com/en-us/windows):
        - For `cmd`, run the following command:

            ```bash
            venv\Scripts\activate.bat
            ```

        - For `powershell`, run the following command:

            ```bash
            venv\Scripts\activate.ps1
            ```

        - For `powershell core`, run the following command:

            ```bash
            venv/bin/Activate.ps1
            ```

    - For [Mac](https://www.apple.com/mac/)/[Linux](https://www.linux.org/)
        - For `bash/zsh`, run the following command:

            ```bash
            source venv/bin/activate
            ```

        - For `fish`, run the following command:

            ```bash
            source venv/bin/activate.fish
            ```

        - For `csh/tcsh`, run the following command:

            ```bash
            source venv/bin/activate.csh
            ```

- Install the project and its python dependencies by running the following commands:

    ```bash
    python3 -m pip install git+https://www.github.com/${user}/${repo_name}
    python3 -m pip install --upgrade pip
    python3 -m pip cache purge
    ```

- And you're done! You can now use the project. Check the [usage](#section) for examples on how to use this project.

${TODO}
## **Contributions**

You can contribute by creating a new issue, or by creating pull requests.

At the time of writing, there are no templates for both creating a new issue and pull requests.

The developer notes however that the said template will be created if a trend of users using this project is evident.

For creating a new issue, please make sure that the said issue is not on the list of closed and open issues.

After checking that that is the case, create a new issue.

The title of the issue must summarize its contents.

The body must contain the following:

- a clear description of the bug
- Python version used for running and/or testing the project
- OS name and version

<!-- Mention the issus and limitations of this repository. Preferrably 1-5 sentences long. -->
## **Known Issues and Limitations**

At the time of writing, this project can not be run in Termux due to a fatal error.

Also, something is broken and I don't know what is, 'cause I forgot!

<!-- Mention the plans for the repository. Preferrably 2-5 sentences long. -->
## **Future of this project**

The TODO will be done, except for that, nothing else.

<!-- License section. Leave unchanged except when updating the year, using a different license, or changing the style altogether. -->
## **License**

### <a target="_blank" href="https://choosealicense.com/licenses/mit/">MIT</a>

${cholder}

Check the [LICENSE](LICENSE.md) for more details.

## **Credits**

### Thank you:

- To [Arjix](https://github.com/ArjixWasTaken), who helped me in implementing majority of the features and de-minifying my code, making it more readable and more efficient at the same time
- To [KR](https://github/com/justfoolingaround), who let me use the KR-naming scheme like "AnimDL" do
- To whi~nyaan, my alter ego, for just existing (and purring, ofc)
- And to everyone who supported me from the very beginning of this humble project to its release!

### MIT Logo

<a target="_blank" href="https://commons.wikimedia.org/wiki/File:MIT_logo.svg">Massachusetts Institute of Technology</a> (vectorized by <a target="_blank" href="https://en.wikipedia.org/wiki/User:Mysid">Mysid</a>, modified by [${user}](https://github.com/${user})), Public domain, via Wikimedia Commons

### Icons

<a target="_blank" href="https://icons8.com/icon/102502/exclamation-mark">Exclamation Mark</a>, <a target="_blank" href="https://icons8.com/icon/33294/code-fork">Code Fork</a>, <a target="_blank" href="https://icons8.com/icon/85185/star">Star</a>, <a target="_blank" href="https://icons8.com/icon/34095/group">Group</a>, <a target="_blank" href="https://icons8.com/icon/87276/code">Code</a>, and <a href="https://icons8.com/icon/30888/discord">Discord</a> icons by <a target="_blank" href="https://icons8.com">Icons8</a>

<sub>
    <i>
        <b>NOTE:</b> If a reference or source material is not attributed properly or not at all, please kindly message me at Discord: <a target="_blank" href="${dc_link}">${dc_acc}</a> (or create a pull request, but at the moment there are no template for pull request so creating one I suppose would be hard) so I can properly give credit to their respective authors.
    </i>
</sub>
