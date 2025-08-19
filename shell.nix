{
  pkgs ? import <nixpkgs> { },
  fetchFromGitHub,
}:

with pkgs.python3Packages;

let
  manim_fork = buildPythonPackage rec {
    pname = "manim";
    version = "0.19.0";
    src = fetchFromGitHub {
      owner = "behackl";
      repo = "manim";
      rev = "codemobject-fix-paragraph-lines";
      hash = "sha256-rxHB95EJP8n6nU7KegehNp2UTpbBVz/85b1fd1T9YJ4=";
    };

    format = "pyproject";
    build-system = [
      hatchling
    ];

    buildInputs = [
      hatchling
    ];

    propagatedBuildInputs = with pkgs; [
      pygments
      scipy
      pydub
      rich
      numpy
      pycairo
      ipython
      pillow
      click
      av
      beautifulsoup4
      cloup
      isosurfaces
      manimpango
      mapbox-earcut
      moderngl
      moderngl-window
      networkx
      screeninfo
      skia-pathops
      python312Packages.srt
      svgelements
      tqdm
      typing-extensions
      python312Packages.watchdog
    ];
  };

  manim_utils = buildPythonPackage rec {
    pname = "manim_utils";
    version = "0.1.0";
    src = fetchFromGitHub {
      owner = "Getting-to-One";
      repo = "manim_utils";
      rev = "main";
      hash = "sha256-OsIR+u+x8bVk86Ocugzl4waEnlV/k2KBuevcOAO0Yl8=";
    };
    doCheck = false;
    format = "pyproject";
    buildInputs = [
      setuptools
    ];
    propagatedBuildInputs = [
      manim_fork
    ];
  };
in
pkgs.mkShell {
  packages = with pkgs; [
    python3
    manim_fork
    manim_utils
  ];
}