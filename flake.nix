{
  description = "Tapis Tutorials Flake";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        
        # Ruby environment with Jekyll
        rubyEnv = pkgs.ruby_3_4.withPackages (ps: with ps; [
          jekyll
          github-pages
          webrick
        ]);
        
        commonPackages = [
          rubyEnv
          pkgs.git
          pkgs.gnugrep
          pkgs.ripgrep
          pkgs.fd
          pkgs.which
        ] ++ pkgs.lib.optional pkgs.stdenv.isDarwin pkgs.darwin.cctools;

        helpText = ''
          \033[34mTapis Tutorials - GitHub Pages Development Environment\033[0m
          
          Development commands:
          ==========================
            - bundle install: Install dependencies from Gemfile
            - bundle exec jekyll serve [--incremental]: Start Jekyll server manually [for live reload]
            - bundle exec jekyll build: Build site manually
            - jekyll clean: Clean generated _site/ directory
            
          Other commands:
          ==========================
            - menu: Show this help message
            - menu --version: Show Ruby, Jekyll, and gem versions
            - nix develop -i: Enter isolated nix shell (ignore user environment)
            - nix develop .#menu: Run 'menu --version' in nix shell
            - nix flake show: View flake outputs
        '';
        
        tapisuiHelpMsg = builtins.replaceStrings ["\n"] ["\\n"] helpText;

        # menu script package with an optional version parameter
        tapisMenu = pkgs.writeScriptBin "menu" ''
          #!${pkgs.bash}/bin/bash
          
          # if input $1 is version or --version, show versions
          if [[ "$1" == "version" || "$1" == "--version" ]]; then
            echo -e "\033[34mVersion Information:\033[0m"
            echo -e "Ruby: $(${rubyEnv}/bin/ruby --version)"
            echo -e "Gem: $(${rubyEnv}/bin/gem --version)"
            echo -e "Jekyll: $(${rubyEnv}/bin/jekyll --version)"
            echo ""
          fi
          
          echo -e "${tapisuiHelpMsg}"
        '';
                
      in {
        devShells = {
          default = pkgs.mkShell {
            packages = commonPackages ++ [
              tapisMenu
            ];
            shellHook = ''
              menu version
            '';
          };
          
          menu = pkgs.mkShell {
            packages = commonPackages ++ [ tapisMenu ];
            shellHook = ''
              menu --version
              exit
            '';
          };
        };
      }
    );
}