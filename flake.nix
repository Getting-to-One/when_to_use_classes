{
  inputs.nixpkgs.url = "github:NixOS/nixpkgs";

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
      devShells.x86_64-linux.default = pkgs.callPackage (self + "/shell.nix") {};
    };
}
