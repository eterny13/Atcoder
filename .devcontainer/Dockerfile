FROM mcr.microsoft.com/devcontainers/base:debian-12

USER vscode

# install haskell
RUN curl --proto '=https' --tlsv1.2 -sSf https://get-ghcup.haskell.org | BOOTSTRAP_HASKELL_NONINTERACTIVE=1 BOOTSTRAP_HASKELL_GHC_VERSION=latest BOOTSTRAP_HASKELL_CABAL_VERSION=latest BOOTSTRAP_HASKELL_INSTALL_STACK=1 BOOTSTRAP_HASKELL_INSTALL_HLS=1 BOOTSTRAP_HASKELL_ADJUST_BASHRC=1 sh

ENV PATH="/root/.ghcup/bin:${PATH}"
RUN echo 'export PATH="$HOME/.ghcup/bin:$PATH"' >> ~/.bashrc
