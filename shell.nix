{ pkgs ? import <nixpkgs> { }, fetchFromGitHub }:
with pkgs.python3Packages;

let manim_utils = buildPythonPackage rec {
  pname = "manim_utils";
  version = "0.1.0";
  src = fetchFromGitHub {
    owner = "Getting-to-One";
    repo = "manim_utils";
    rev = "main";
    hash = "sha256-g56FMBQ7ni+lxqfWiF4dyJilZuRuKL5XXZcHcDUSPME=";
  };
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
