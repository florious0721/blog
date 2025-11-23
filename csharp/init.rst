.. include:: refs.rst

环境配置
########

安装 SDK
--------

从 `官网 <dotnet_>`_ 或包管理器安装 .NET SDK，
建议安装一个最新版用于提供语言服务，例如 `语言服务器 <roslyn-ls-nuget_>`_，
再安装一个最新 LTS 版用于开发。

语言服务器
----------

推荐使用 `微软官方的语言服务器 <roslyn-ls-nuget_>`_，
omnisharp_ 还以 ``net6.0`` 作为目标框架，
csharp-ls_ 的反应不是很快，而且似乎不支持 Godot_ 项目。

可以通过 `Nuget <roslyn-ls-nuget_>`_ 或 `Azure <roslyn-ls-azure_>`_
下载语言服务器，解压后确保 :file:`Microsoft.CodeAnalysis.LanguageServer`
在你的 :envvar:`PATH` 中即可。

`Neovim_ <nvim-lsp-roslyn_>`_ 配置
----------------------------------

在你的 `LSP 配置 <nvim-lsp_>`_ 中添加
:code:`vim.lsp.enable('roslyn_ls')` 即可，开箱即用。
