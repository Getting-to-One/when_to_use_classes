{
  inputs.nixpkgs = {
    type = "github";
    owner = "NixOS";
    repo = "nixpkgs";
    rev = "21808d22b1cda1898b71cf1a1beb524a97add2c4"; 
  };

  outputs =
    inputs@{
      self,
      nixpkgs,
      ...
    }:
    let
      pkgs = inputs.nixpkgs.legacyPackages.x86_64-linux;
    in
    {
      devShells.x86_64-linux.default = pkgs.callPackage (self + "/shell.nix") { };
    };
}
