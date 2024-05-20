# PretaMap

## Overview

PretaMap is a popup imagemap tool specifically designed for Plone content. It allows developers to add interactive imagemaps to their Plone websites, enhancing user engagement through visual interactivity.

## Features

- Easy integration with Plone CMS.
- Supports interactive imagemaps with popup tooltips.
- Utilizes jQuery for frontend interactivity.
- Customizable tooltip behavior and styling.

## Installation Instructions

Follow these steps to set up PretaMap:

1. **Clone the Repository**: First, clone the repository to your local machine.
    ```sh
    git clone https://github.com/Yuriy/pretaweb.pretamap.git
    cd pretaweb.pretamap
    ```

2. **Install Dependencies**: Make sure you have setuptools installed. Run the following command to install the package.
    ```sh
    python setup.py install
    ```

3. **Configure Plone**: Configure your Plone site to include the PretaMap module. Add necessary configurations to your buildout.

4. **Run Buildout**: Finally, run buildout to apply the configurations.
    ```sh
    ./bin/buildout
    ```

## Usage Examples

Using PretaMap in your Plone site can be quite straightforward. Here's a quick example of how to set up an imagemap with tooltips:

1. **Include the JS and CSS**:
    Make sure to include the necessary JavaScript and CSS files in your Plone site's template.
    ```html
    <script src="path/to/jquery.qtip-1.0.0-rc3.min.js"></script>
    <script src="path/to/pretamap.js"></script>
    <link rel="stylesheet" href="path/to/pretamap.css">
    ```

2. **Define An Imagemap**:
    ```html
    <img src="yourimage.jpg" usemap="#imagemap">
    <map name="imagemap">
        <area shape="rect" coords="34,44,270,350" href="#point1">
        <area shape="rect" coords="290,172,333,250" href="#point2">
    </map>
    
    <!-- Tooltip Contents -->
    <div class="popup">
        <a name="point1"></a>
        <div>Point 1 Info...</div>
    </div>
    <div class="popup">
        <a name="point2"></a>
        <div>Point 2 Info...</div>
    </div>
    ```

3. **Initialize PretaMap**:
    ```js
    jQuery(document).ready(function($) {
        jQuery(".pretamap AREA").each( function() {
            var anchor = $(this).attr('href').substring(1);
            var tip = 'div.popup:has(a[name="'+anchor+'"])';
            <snippet for tooltip settings>;
        });
    });
    ```
    
## Code Summary

The code structure of PretaMap is straightforward:

- **setup.py**: Handles the setup and installation of the package.
- **pretaweb/__init__.py**: Declares the namespace package.
- **pretaweb/pretamap/setuphandlers.py**: Contains setup handlers for the package.
- **pretaweb/pretamap/tests.py**: Provides unit tests for the package.
- **pretaweb/pretamap/browser/**: Contains browser-related files:
  - `interfaces.py`: Defines browser layer interfaces.
  - `jquery.qtip-1.0.0-rc3.min.js`: Minified jQuery QTip library for tooltips.
  - `pretamap.js`: Main JavaScript file to initialize and handle imagemap tooltips.

## Contributing Guidelines

We welcome contributions to make PretaMap better! If you're interested in contributing, please follow these steps:

1. **Fork the Repository**: Fork the repository on GitHub.
2. **Clone Your Fork**: Clone your forked repository to your local machine.
    ```sh
    git clone https://github.com/YourUsername/pretaweb.pretamap.git
    cd pretaweb.pretamap
    ```
3. **Create a Branch**: Create a new branch for your feature or bugfix.
    ```sh
    git checkout -b feature/your-feature-name
    ```
4. **Make Your Changes**: Make your changes to the codebase.
5. **Commit Your Changes**: Commit your changes with a descriptive commit message.
    ```sh
    git commit -m "Add feature X to improve Y"
    ```
6. **Push to Your Fork**: Push your changes to your fork.
    ```sh
    git push origin feature/your-feature-name
    ```
7. **Submit a Pull Request**: Open a pull request on the original repository with a description of your changes.

## License

PretaMap is open source and available under the MIT License. For more details, see the [LICENSE](LICENSE) file.

---

Thank you for using PretaMap! If you have any issues or questions, feel free to open an issue on GitHub.