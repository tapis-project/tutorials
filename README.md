# Tapis Tutorials

[Tapis](https://tapis-project.org) is an NSF-funded API platform for computational research. It provides a comprehensive suite of services for managing authentication, systems, files, applications, jobs, and workflows across distributed computing resources. Tapis enables collaboration on HPC, ML, and Research workloads.

## Tutorial Hub

Over the years, Tapis tutorials have been delivered at various conferences and workshops. To ensure users have access to current, accurate information about Tapis capabilities, it's encouraged to view the current latest tutorial. Tutorials are archived and listed here for historical record. Archived tutorials might contain additional and unique information, but might as well be out-of-date, be aware.

The latest tutorial is available at: [https://tapis-project.github.io/tutorials](https://tapis-project.github.io/tutorials/)

This is a list of some archived Tapis tutorial repositories, ordered by recency:

| Tutorial | Date | Description |
|----------|------|-------------|
| [PEARC25](https://github.com/tapis-project/pearc25-tapis-tutorial) | 2025-07 | 2025 PEARC tutorial |
| [TACCSTER24](https://github.com/tapis-project/taccster24-tapis-tutorial) | 2024-09 | TACCSTER24 tutorial |
| [PEARC24](https://github.com/tapis-project/pearc24-tapis-tutorial) | 2024-07 | PEARC24 Tapis tutorial |
| [SGX3](https://github.com/tapis-project/sgx3-tapis-tutorial) | 2024-06 | Science Gateways tutorial |
| [Tapis ML](https://github.com/tapis-project/tapis-ml-tutorial) | 2024-06 | Tapis tutorial explaining ML workflow |
| [Gateways24](https://github.com/tapis-project/gateways24-tapis-tutorial) | 2024-02 | Gateways conference tutorial |
| [Workflows](https://github.com/tapis-project/workflows-tutorial) | 2023-10 | CI/CD for High Performance Computation with Tapis Workflows API |
| [PEARC20](https://github.com/tapis-project/pearc20-tapis-tutorial) | 2020-07 | Portable, Reproducible HPC in the Cloud |

## Deployment (GH Pages and Local)
#### Github Pages
A tutorial page can be deployed via Github Pages by navigating to repository Settings -> Pages -> Build and Deployment -> Branch (select current) -> Set folder to `/docs`.

Currently only `/` or `/docs` are hosted by gh pages. You can also create a github action that publishes a gh-pages branch if preferred. This means that a user must move tutorial to `/docs` to be rendered by GH pages.

#### Local Development
A tutorial page can also be deployed locally for development or for viewing by using Jekyll. Each tutorial folder should contain a Gemfile for use with the Ruby programming language. You'll need to ensure Ruby, Gem, and bundle are installed and accessible.

```
# 1. navigate to preferred tutorial folder
$ cd 2022-10-tutorial

# 2. install dependencies
$ bundle install

# 3. deploy the page by default to localhost:4000
$ bundle exec jekyll serve
```

#### Local Development (with Nix)
Nix is a package manager which is utilized to provide an environment declared by `flake.nix` that provides Ruby, Gem, and bundle in an isolated shell. The shell provided also contains helper messages as shown below. You will need to have `nix` installed. Once you've entered the shell, you can run steps 1, 2, 3 from before without issue.

```
# 0. enter the shell from repo root, afterwards, run steps 1, 2, 3 from before
$ nix develop

Version Information:
Ruby: ruby 3.4.7
Gem: 3.7.1
Jekyll: jekyll 3.1.6

Tapis Tutorials - GitHub Pages Development Environment

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
```


## Contributing

If you find issues with the current tutorial or have suggestions for improvements, please open an issue in the [tutorials repository](https://github.com/tapis-project/tutorials/issues).