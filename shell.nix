{ pkgs ? import <nixpkgs> { } }:
with pkgs.python3Packages;

let manim_utils = buildPythonPackage rec {
  pname = "manim_utils";
  version = "0.1.0";
  src = ../manim_utils;
  doCheck = false; # check requires pip
  format = "pyproject";
  buildInputs = [
    setuptools
  ];
  propagatedBuildInputs = [
    manim
  ];
};
in
pkgs.mkShell {
  packages = with pkgs; [
    python3
    manim
    manim_utils
  ];
}