.NET
####

* 将当前目录初始化为 .NET 项目

  :code:`dotnet new console`

* 添加项目引用

  :samp:`dotnet add reference {FNA.Core.csproj}`

* 添加 DLL 引用

  .. code:: xml

    <ItemGroup>
      <Reference Inlucde="Example.dll"/>
    </ItemGroup>

* 构建项目

  :samp:`dotnet build {FNA.Core.csproj}`

  若不指定项目文件则会在当前目录下搜索，搜索到多个时会报错。
