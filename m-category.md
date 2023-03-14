# Power Query M 函数文档(功能分类版)
<h2 id="home"><a href="https://jiaopengzi.com/doc" class="a-button">点击返回主页</a></h2><span id="jiaopengzi"><a href="https://jiaopengzi.com/">焦棚子</a>整理</span>
<h2 id="content">目录</h2>
| **<a href="#1">1、数据访问函数(81)</a>** | **<a href="#2">2、文本函数(45)</a>** | **<a href="#3">3、二进制函数(39)</a>** |
| :--: | :--: |:--: |
| **<a href="#4">4、合并器函数(5)</a>** | **<a href="#5">5、比较器函数(4)</a>** | **<a href="#6">6、日期函数(58)</a>** |
| **<a href="#7">7、日期/时间函数(26)</a>** | **<a href="#8">8、日期/时间/时区函数(16)</a>** | **<a href="#9">9、持续时间函数(13)</a>** |
| **<a href="#10">10、错误处理函数(3)</a>** | **<a href="#11">11、表达式函数(3)</a>** | **<a href="#12">12、函数值(5)</a>** |
| **<a href="#13">13、行函数(4)</a>** | **<a href="#14">14、列表函数(71)</a>** | **<a href="#15">15、逻辑函数(3)</a>** |
| **<a href="#16">16、数字函数(52)</a>** | **<a href="#17">17、记录函数(23)</a>** | **<a href="#18">18、替换器函数(2)</a>** |
| **<a href="#19">19、拆分器函数(10)</a>** | **<a href="#20">20、表函数(117)</a>** | **<a href="#21">21、时间函数(10)</a>** |
| **<a href="#22">22、类型函数(22)</a>** | **<a href="#23">23、Uri 函数(4)</a>** | **<a href="#24">24、值函数(34)</a>** |
<h2 id='1'>1、数据访问函数</h2>
<a href='#content'>返回目录</a>
| 函数名称 | 描述 | 链接 |
| :--: | :--: |:--: |
| AccessControlEntry.ConditionToIdentities | 使用指定的 identityProvider，将 condition 转换为一个标识列表；对于该列表，condition 在以 identityProvider 作为标识提供程序的所有授权上下文中都将返回 true。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/accesscontrolentry-conditiontoidentities) [英文](https://learn.microsoft.com/en-us/powerquery-m/accesscontrolentry-conditiontoidentities) |
| Access.Database | 返回 Access 数据库 database 的结构表示形式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/access-database) [英文](https://learn.microsoft.com/en-us/powerquery-m/access-database) |
| ActiveDirectory.Domains | 返回与指定域或当前计算机的域（如果未指定任何域）处于同一个林中的 Active Directory 域的列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/activedirectory-domains) [英文](https://learn.microsoft.com/en-us/powerquery-m/activedirectory-domains) |
| AdobeAnalytics.Cubes | 从 Adobe Analytics 返回多维包的表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/adobeanalytics-cubes) [英文](https://learn.microsoft.com/en-us/powerquery-m/adobeanalytics-cubes) |
| AdoDotNet.DataSource | 返回 ADO.NET 数据源的架构集合，其中包含提供程序名称 providerName 和连接字符串 connectionString。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/adodotnet-datasource) [英文](https://learn.microsoft.com/en-us/powerquery-m/adodotnet-datasource) |
| AdoDotNet.Query | 返回使用 ADO.NET 提供程序 providerName 通过连接字符串 connectionString 运行 query 的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/adodotnet-query) [英文](https://learn.microsoft.com/en-us/powerquery-m/adodotnet-query) |
| AnalysisServices.Database | 从服务器 server 上的 Analysis Services 数据库 database 中返回多维数据集或表格模型的表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/analysisservices-database) [英文](https://learn.microsoft.com/en-us/powerquery-m/analysisservices-database) |
| AnalysisServices.Databases | 返回 Analysis Services 实例 server 上的数据库。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/analysisservices-databases) [英文](https://learn.microsoft.com/en-us/powerquery-m/analysisservices-databases) |
| AzureStorage.BlobContents | 从 Azure 存储库返回 URL 处的 blob 的内容 url。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/azurestorage-blobcontents) [英文](https://learn.microsoft.com/en-us/powerquery-m/azurestorage-blobcontents) |
| AzureStorage.Blobs | 返回一个导航表，对于从 Azure 存储库中的帐户 URL account 处找到的每个容器，都作为一行包含在此表中。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/azurestorage-blobs) [英文](https://learn.microsoft.com/en-us/powerquery-m/azurestorage-blobs) |
| AzureStorage.DataLake | 返回一个导航表，其中包含在 Azure Data Lake Storage 文件系统的指定容器及其帐户 URL endpoint 处的子文件夹中找到的文档。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/azurestorage-datalake) [英文](https://learn.microsoft.com/en-us/powerquery-m/azurestorage-datalake) |
| AzureStorage.DataLakeContents | 从 Azure Data Lake Storage 文件系统返回 URL 处文件的内容 url。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/azurestorage-datalakecontents) [英文](https://learn.microsoft.com/en-us/powerquery-m/azurestorage-datalakecontents) |
| AzureStorage.Tables | 返回一个导航表，它对于在 Azure 存储库的帐户 URL account 上找到的每个表包含一行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/azurestorage-tables) [英文](https://learn.microsoft.com/en-us/powerquery-m/azurestorage-tables) |
| Cdm.Contents | 此函数不可用，因为它需要使用 .NET 4.5。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/cdm-contents) [英文](https://learn.microsoft.com/en-us/powerquery-m/cdm-contents) |
| Csv.Document | 返回 CSV 文档的内容作为表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/csv-document) [英文](https://learn.microsoft.com/en-us/powerquery-m/csv-document) |
| Cube.AddAndExpandDimensionColumn | 将指定维度表 dimensionSelector 合并到多维数据集 cube 的筛选上下文中，并通过展开指定维度属性集 attributeNames 来更改维度粒度。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/cube-addandexpanddimensioncolumn) [英文](https://learn.microsoft.com/en-us/powerquery-m/cube-addandexpanddimensioncolumn) |
| Cube.AddMeasureColumn | 向 cube 添加包含名称 column 的列，其中包含在每行的行上下文中应用的度量值 measureSelector 的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/cube-addmeasurecolumn) [英文](https://learn.microsoft.com/en-us/powerquery-m/cube-addmeasurecolumn) |
| Cube.ApplyParameter | 通过将 parameter 与 arguments 应用到 cube 后返回多维数据集。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/cube-applyparameter) [英文](https://learn.microsoft.com/en-us/powerquery-m/cube-applyparameter) |
| Cube.AttributeMemberId | 从成员属性值返回唯一的成员标识符。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/cube-attributememberid) [英文](https://learn.microsoft.com/en-us/powerquery-m/cube-attributememberid) |
| Cube.AttributeMemberProperty | 返回维度属性 attribute 的属性 propertyName。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/cube-attributememberproperty) [英文](https://learn.microsoft.com/en-us/powerquery-m/cube-attributememberproperty) |
| Cube.CollapseAndRemoveColumns | 通过折叠映射至指定列 columnNames 的属性，更改 cube 筛选上下文的维度粒度。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/cube-collapseandremovecolumns) [英文](https://learn.microsoft.com/en-us/powerquery-m/cube-collapseandremovecolumns) |
| Cube.Dimensions | 返回包含 cube 中可用维度集的表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/cube-dimensions) [英文](https://learn.microsoft.com/en-us/powerquery-m/cube-dimensions) |
| Cube.DisplayFolders | 返回一个表嵌套树，它表示可在 cube 中使用的对象（如维度和度量值）的显示文件夹层次结构。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/cube-displayfolders) [英文](https://learn.microsoft.com/en-us/powerquery-m/cube-displayfolders) |
| Cube.MeasureProperties | 返回一个表，此表包含在多维数据集中扩展的度量值的可用属性集。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/cube-measureproperties) [英文](https://learn.microsoft.com/en-us/powerquery-m/cube-measureproperties) |
| Cube.MeasureProperty | 返回度量值 measure 的属性 propertyName。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/cube-measureproperty) [英文](https://learn.microsoft.com/en-us/powerquery-m/cube-measureproperty) |
| Cube.Measures | 返回包含 cube 中可用度量值集的表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/cube-measures) [英文](https://learn.microsoft.com/en-us/powerquery-m/cube-measures) |
| Cube.Parameters | 返回一个表，此表包含可应用到 cube 的参数集。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/cube-parameters) [英文](https://learn.microsoft.com/en-us/powerquery-m/cube-parameters) |
| Cube.Properties | 返回一个表，此表包含在多维数据集中扩展的维度的可用属性集。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/cube-properties) [英文](https://learn.microsoft.com/en-us/powerquery-m/cube-properties) |
| Cube.PropertyKey | 返回属性 property 的键。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/cube-propertykey) [英文](https://learn.microsoft.com/en-us/powerquery-m/cube-propertykey) |
| Cube.ReplaceDimensions | 替换 Cube.Dimensions 返回的一组维度。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/cube-replacedimensions) [英文](https://learn.microsoft.com/en-us/powerquery-m/cube-replacedimensions) |
| Cube.Transform | 在 cube 上应用多维数据集函数列表 transforms。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/cube-transform) [英文](https://learn.microsoft.com/en-us/powerquery-m/cube-transform) |
| DB2.Database | 返回 SQL 表和视图的表，此表在名为 database 的数据库实例中的服务器 server 上的 Db2 数据库中可用。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/db2-database) [英文](https://learn.microsoft.com/en-us/powerquery-m/db2-database) |
| Essbase.Cubes | 返回一个多维数据集表，其中的数据集由 Essbase 服务器根据 APS 服务器 url 上的 Essbase 实例进行分组。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/essbase-cubes) [英文](https://learn.microsoft.com/en-us/powerquery-m/essbase-cubes) |
| Excel.CurrentWorkbook | 返回当前 Excel 工作簿的内容。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/excel-currentworkbook) [英文](https://learn.microsoft.com/en-us/powerquery-m/excel-currentworkbook) |
| Excel.Workbook | 返回 Excel 工作簿的内容。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/excel-workbook) [英文](https://learn.microsoft.com/en-us/powerquery-m/excel-workbook) |
| Exchange.Contents | 返回来自 Microsoft Exchange 帐户 mailboxAddress 的目录。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/exchange-contents) [英文](https://learn.microsoft.com/en-us/powerquery-m/exchange-contents) |
| File.Contents | 以二进制形式返回文件 path 的内容。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/file-contents) [英文](https://learn.microsoft.com/en-us/powerquery-m/file-contents) |
| Folder.Contents | 返回一个表，其中包含在文件夹 path 中找到的每个文件夹和文件的行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/folder-contents) [英文](https://learn.microsoft.com/en-us/powerquery-m/folder-contents) |
| Folder.Files | 返回一个表，其中包含在文件夹 path 及其所有子文件夹中找到的每个文件的行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/folder-files) [英文](https://learn.microsoft.com/en-us/powerquery-m/folder-files) |
| GoogleAnalytics.Accounts | 返回可通过当前凭据进行访问的 Google Analytics 帐户。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/googleanalytics-accounts) [英文](https://learn.microsoft.com/en-us/powerquery-m/googleanalytics-accounts) |
| Hdfs.Contents | 返回一个表，其中包含在 Hadoop 文件系统的文件夹 URL 和 url 中找到的每个文件夹和文件的行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/hdfs-contents) [英文](https://learn.microsoft.com/en-us/powerquery-m/hdfs-contents) |
| Hdfs.Files | 返回一个表，其中包含在 Hadoop 文件系统的文件夹 URL、url 和子文件夹中找到的每个文件的行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/hdfs-files) [英文](https://learn.microsoft.com/en-us/powerquery-m/hdfs-files) |
| HdInsight.Containers | 返回一个导航表，对于从 Azure 存储库中的帐户 URL account 处找到的每个容器，都作为一行包含在此表中。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/hdinsight-containers) [英文](https://learn.microsoft.com/en-us/powerquery-m/hdinsight-containers) |
| HdInsight.Contents | 返回一个导航表，对于从 Azure 存储库中的帐户 URL account 处找到的每个容器，都作为一行包含在此表中。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/hdinsight-contents) [英文](https://learn.microsoft.com/en-us/powerquery-m/hdinsight-contents) |
| HdInsight.Files | 返回一个表，对于从 Azure 存储库中的容器 URL account 处找到的每个 blob 文件，都作为一行包含在此表中。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/hdinsight-files) [英文](https://learn.microsoft.com/en-us/powerquery-m/hdinsight-files) |
| Html.Table | 返回一个表，其中包含针对所提供的 html 运行指定 CSS 选择器的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/html-table) [英文](https://learn.microsoft.com/en-us/powerquery-m/html-table) |
| Identity.From | 创建标识。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/identity-from) [英文](https://learn.microsoft.com/en-us/powerquery-m/identity-from) |
| Identity.IsMemberOf | 确定某标识是否为某一标识集合的成员。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/identity-ismemberof) [英文](https://learn.microsoft.com/en-us/powerquery-m/identity-ismemberof) |
| IdentityProvider.Default | 当前主机的默认标识提供程序。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/identityprovider-default) [英文](https://learn.microsoft.com/en-us/powerquery-m/identityprovider-default) |
| Informix.Database | 返回 SQL 表和视图的一个表，这些表和视图在名为 database 数据库实例中服务器 server 上的 Informix 数据库中可用。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/informix-database) [英文](https://learn.microsoft.com/en-us/powerquery-m/informix-database) |
| Json.Document | 返回 JSON 文档的内容。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/json-document) [英文](https://learn.microsoft.com/en-us/powerquery-m/json-document) |
| MySQL.Database | 在名为 database 的数据库实例中，返回服务器 server 上 MySQL 数据库中可用的 SQL 表、视图和存储标量函数的表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/mysql-database) [英文](https://learn.microsoft.com/en-us/powerquery-m/mysql-database) |
| OData.Feed | 从 URI serviceUri、标头 headers 返回 OData 服务提供的 OData 源表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/odata-feed) [英文](https://learn.microsoft.com/en-us/powerquery-m/odata-feed) |
| Odbc.DataSource | 从连接字符串 connectionString 指定的 ODBC 数据源中返回 SQL 表和视图的表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/odbc-datasource) [英文](https://learn.microsoft.com/en-us/powerquery-m/odbc-datasource) |
| Odbc.InferOptions | 返回后列推断的结果：尝试通过使用 ODBC 的连接字符串 connectionString 来推断 SQL 功能。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/odbc-inferoptions) [英文](https://learn.microsoft.com/en-us/powerquery-m/odbc-inferoptions) |
| Odbc.Query | 返回在 ODBC 中使用连接字符串 connectionString 运行 query 的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/odbc-query) [英文](https://learn.microsoft.com/en-us/powerquery-m/odbc-query) |
| OleDb.DataSource | 返回 SQL 表的表并从由连接字符串 connectionString 指定的 OLE DB 数据源进行查看。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/oledb-datasource) [英文](https://learn.microsoft.com/en-us/powerquery-m/oledb-datasource) |
| OleDb.Query | 返回在 OLE DB 中使用连接字符串 connectionString 运行 query 的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/oledb-query) [英文](https://learn.microsoft.com/en-us/powerquery-m/oledb-query) |
| Oracle.Database | 从服务器 server 上的 Oracle Database 中返回 SQL 表和视图的表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/oracle-database) [英文](https://learn.microsoft.com/en-us/powerquery-m/oracle-database) |
| Pdf.Tables | 返回 pdf 中找到的任何表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/pdf-tables) [英文](https://learn.microsoft.com/en-us/powerquery-m/pdf-tables) |
| PostgreSQL.Database | 返回包含 SQL 表和视图的表，这些表和视图在名为 database 数据库实例中服务器 server 上的 PostgreSQL 数据库中可用。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/postgresql-database) [英文](https://learn.microsoft.com/en-us/powerquery-m/postgresql-database) |
| RData.FromBinary | 从 RData 文件返回数据帧记录。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/rdata-frombinary) [英文](https://learn.microsoft.com/en-us/powerquery-m/rdata-frombinary) |
| Salesforce.Data | 返回凭据中提供的 Salesforce 帐户的对象。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/salesforce-data) [英文](https://learn.microsoft.com/en-us/powerquery-m/salesforce-data) |
| Salesforce.Reports | 返回凭据中提供的 Salesforce 帐户的报表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/salesforce-reports) [英文](https://learn.microsoft.com/en-us/powerquery-m/salesforce-reports) |
| SapBusinessWarehouse.Cubes | 返回一个表，此表包含在服务器 server 处的一个 SAP Business Warehouse 实例中按 InfoArea 分组的 InfoCubes 和查询，系统编号为 systemNumberOrSystemId，客户端 ID 为 clientId。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/sapbusinesswarehouse-cubes) [英文](https://learn.microsoft.com/en-us/powerquery-m/sapbusinesswarehouse-cubes) |
| SapHana.Database | 从 SAP HANA 数据库 server 返回多维包的表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/saphana-database) [英文](https://learn.microsoft.com/en-us/powerquery-m/saphana-database) |
| SharePoint.Contents | 返回一个表，该表包含在指定 SharePoint 站点 url 中找到的每个文件夹和文档的行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/sharepoint-contents) [英文](https://learn.microsoft.com/en-us/powerquery-m/sharepoint-contents) |
| SharePoint.Files | 返回一个表，其中包含在指定 SharePoint 站点 url 和子文件夹中找到的每个文档的行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/sharepoint-files) [英文](https://learn.microsoft.com/en-us/powerquery-m/sharepoint-files) |
| SharePoint.Tables | 返回一个表，该表包含在指定 SharePoint 列表 url 处找到的每个列表项的行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/sharepoint-tables) [英文](https://learn.microsoft.com/en-us/powerquery-m/sharepoint-tables) |
| Soda.Feed | 从位于指定 URL url（根据 SODA 2.0 API 进行格式化）的内容中返回一个表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/soda-feed) [英文](https://learn.microsoft.com/en-us/powerquery-m/soda-feed) |
| Sql.Database | 从服务器 server 上的 SQL Server 数据库 database 中返回 SQL 表、视图和存储函数的表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/sql-database) [英文](https://learn.microsoft.com/en-us/powerquery-m/sql-database) |
| Sql.Databases | 返回指定的 SQL Server server 上的数据库表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/sql-databases) [英文](https://learn.microsoft.com/en-us/powerquery-m/sql-databases) |
| Sybase.Database | 返回 SQL 表和视图的表，该表在名为 database 的数据库实例中的服务器 server 上的 Sybase 数据库中可用。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/sybase-database) [英文](https://learn.microsoft.com/en-us/powerquery-m/sybase-database) |
| Teradata.Database | 从服务器 server 上的 Teradata 数据库中返回 SQL 表和视图的表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/teradata-database) [英文](https://learn.microsoft.com/en-us/powerquery-m/teradata-database) |
| WebAction.Request | 创建以下操作：执行后，将使用 HTTP 针对 url 执行 method 请求的结果作为二进制值返回。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/webaction-request) [英文](https://learn.microsoft.com/en-us/powerquery-m/webaction-request) |
| Web.BrowserContents | 返回 Web 浏览器查看的指定的 url 的 HTML。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/web-browsercontents) [英文](https://learn.microsoft.com/en-us/powerquery-m/web-browsercontents) |
| Web.Contents | 以二进制形式返回从 url 下载的内容。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/web-contents) [英文](https://learn.microsoft.com/en-us/powerquery-m/web-contents) |
| Web.Headers | 返回从 url 下载的标头作为记录。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/web-headers) [英文](https://learn.microsoft.com/en-us/powerquery-m/web-headers) |
| Web.Page | 返回 HTML 文档的内容（分解为其组成结构），以及删除标记后的完整文档及其文本的表示形式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/web-page) [英文](https://learn.microsoft.com/en-us/powerquery-m/web-page) |
| Xml.Document | 返回 XML 文档的内容作为层次结构表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/xml-document) [英文](https://learn.microsoft.com/en-us/powerquery-m/xml-document) |
| Xml.Tables | 返回 XML 文档的内容作为平展表的嵌套集合。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/xml-tables) [英文](https://learn.microsoft.com/en-us/powerquery-m/xml-tables) |
<h2 id='2'>2、文本函数</h2>
<a href='#content'>返回目录</a>
| 函数名称 | 描述 | 链接 |
| :--: | :--: |:--: |
| Json.FromValue | 生成给定值 value 的 JSON 表示形式，其文本编码由 encoding 指定。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/json-fromvalue) [英文](https://learn.microsoft.com/en-us/powerquery-m/json-fromvalue) |
| Character.FromNumber | 返回与该数值等效的字符。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/character-fromnumber) [英文](https://learn.microsoft.com/en-us/powerquery-m/character-fromnumber) |
| Character.ToNumber | 返回与字符 character 等效的数值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/character-tonumber) [英文](https://learn.microsoft.com/en-us/powerquery-m/character-tonumber) |
| Guid.From | 从给定的 value 返回 Guid.Type 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/guid-from) [英文](https://learn.microsoft.com/en-us/powerquery-m/guid-from) |
| Text.AfterDelimiter | 返回 text 中指定 delimiter 后的部分。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-afterdelimiter) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-afterdelimiter) |
| Text.At | 返回在文本值 text 中位于第 index 位的字符。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-at) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-at) |
| Text.BeforeDelimiter | 返回 text 中指定 delimiter 前的部分。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-beforedelimiter) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-beforedelimiter) |
| Text.BetweenDelimiters | 返回指定的 startDelimiter 和 endDelimiter 之间 text 的部分。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-betweendelimiters) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-betweendelimiters) |
| Text.Clean | 返回 text 的所有控制字符均已删除的文本值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-clean) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-clean) |
| Text.Combine | 返回将文本值列表（texts）合并为单个文本值的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-combine) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-combine) |
| Text.Contains | 检测 text 是否包含值 substring 。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-contains) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-contains) |
| Text.End | 返回一个 text 值，该值是 text 值 text 的后 count 个字符。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-end) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-end) |
| Text.EndsWith | 指示给定的文本 text 是否以指定的值 substring 结尾。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-endswith) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-endswith) |
| Text.Format | 返回通过将来自列表或记录的 arguments 应用于格式字符串 formatString 创建的格式化文本。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-format) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-format) |
| Text.From | 返回 value 的文本表示形式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-from) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-from) |
| Text.FromBinary | 使用 encoding 类型将数据 binary 从二进制值解码为文本值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-frombinary) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-frombinary) |
| Text.InferNumberType | 推断 text 的粒度数字类型（Int64.Type、Double.Type 等）。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-infernumbertype) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-infernumbertype) |
| Text.Insert | 返回将文本值 newText 插入到位置 offset 的文本值 text 中的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-insert) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-insert) |
| Text.Length | 返回文本 text 中的字符数。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-length) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-length) |
| Text.Lower | 返回将 text 中的所有字符转换为小写的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-lower) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-lower) |
| Text.Middle | 返回 count 个字符，或返回至 text 的结束；偏移量为 start。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-middle) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-middle) |
| Text.NewGuid | 返回新的、随机的全局唯一标识符 (GUID)。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-newguid) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-newguid) |
| Text.PadEnd | 通过在文本值 text 的末尾插入空格，返回填充到长度 count 的 text 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-padend) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-padend) |
| Text.PadStart | 通过在文本值 text 的开头插入空格，返回填充到长度 count 的 text 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-padstart) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-padstart) |
| Text.PositionOf | 返回在 text 中找到的文本值 substring 的指定出现位置。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-positionof) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-positionof) |
| Text.PositionOfAny | 返回可在 text 中找到的列表 characters 中任何字符的第一个位置。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-positionofany) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-positionofany) |
| Text.Proper | 返回只使文本值 text 中每个字词的第一个字母大写的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-proper) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-proper) |
| Text.Range | 返回在文本 text 中偏移量 offset 处找到的 substring。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-range) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-range) |
| Text.Remove | 返回文本值 text 的副本，其中已删除了 removeChars 中的所有字符。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-remove) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-remove) |
| Text.RemoveRange | 返回文本值 text 已删除了 offset 位置后所有字符的副本。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-removerange) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-removerange) |
| Text.Repeat | 返回由输入文本 text 重复 count 次而组成的文本值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-repeat) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-repeat) |
| Text.Replace | 返回将文本值 text 中所有出现的文本值 old 替换为文本值 new 的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-replace) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-replace) |
| Text.ReplaceRange | 返回从文本值 text 中的位置 offset 开始删除一些字符 count，然后在 text 中的相同位置插入文本值 newText 的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-replacerange) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-replacerange) |
| Text.Reverse | 反写所提供的 text。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-reverse) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-reverse) |
| Text.Select | 返回文本值 text 的副本，其中已删除 selectChars 中不存在的所有字符。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-select) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-select) |
| Text.Split | 返回根据指定的分隔符 separator 拆分文本值 text 而得到的文本值列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-split) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-split) |
| Text.SplitAny | 返回根据指定的分隔符 separators 中的任意字符拆分文本值 text 而得到的文本值列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-splitany) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-splitany) |
| Text.Start | 返回 text 的前 count 个字符作为文本值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-start) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-start) |
| Text.StartsWith | 如果文本值 text 以文本值 substring 开头，则返回 true。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-startswith) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-startswith) |
| Text.ToBinary | 使用指定的 encoding 将给定的文本值 text 编码为二进制值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-tobinary) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-tobinary) |
| Text.ToList | 从给定的文本值 text 返回字符值列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-tolist) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-tolist) |
| Text.Trim | 返回从文本值 text 删除所有前导空格和尾随空格的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-trim) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-trim) |
| Text.TrimEnd | 返回从文本值 text 中删除所有尾随空格的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-trimend) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-trimend) |
| Text.TrimStart | 返回从文本值 text 删除所有前导空格的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-trimstart) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-trimstart) |
| Text.Upper | 返回将 text 中的所有字符转换为大写的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/text-upper) [英文](https://learn.microsoft.com/en-us/powerquery-m/text-upper) |
<h2 id='3'>3、二进制函数</h2>
<a href='#content'>返回目录</a>
| 函数名称 | 描述 | 链接 |
| :--: | :--: |:--: |
| Binary.ApproximateLength | 返回 binary 的近似长度，或者如果数据源不支持近似长度，则返回错误。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binary-approximatelength) [英文](https://learn.microsoft.com/en-us/powerquery-m/binary-approximatelength) |
| Binary.Buffer | 缓冲内存中的二进制值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binary-buffer) [英文](https://learn.microsoft.com/en-us/powerquery-m/binary-buffer) |
| Binary.Combine | 将一系列二进制值合并成单个二进制值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binary-combine) [英文](https://learn.microsoft.com/en-us/powerquery-m/binary-combine) |
| Binary.Compress | 使用给定的压缩类型压缩二进制值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binary-compress) [英文](https://learn.microsoft.com/en-us/powerquery-m/binary-compress) |
| Binary.Decompress | 使用给定压缩类型解压缩二进制值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binary-decompress) [英文](https://learn.microsoft.com/en-us/powerquery-m/binary-decompress) |
| Binary.From | 从给定的 value 返回 binary 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binary-from) [英文](https://learn.microsoft.com/en-us/powerquery-m/binary-from) |
| Binary.FromList | 将一组数值转换为一个二进制值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binary-fromlist) [英文](https://learn.microsoft.com/en-us/powerquery-m/binary-fromlist) |
| Binary.FromText | 返回将文本值 text 转换为二进制的结果（number 列表）。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binary-fromtext) [英文](https://learn.microsoft.com/en-us/powerquery-m/binary-fromtext) |
| Binary.InferContentType | 返回一条记录，其中的 Content.Type 字段包含推理出的 MIME 类型。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binary-infercontenttype) [英文](https://learn.microsoft.com/en-us/powerquery-m/binary-infercontenttype) |
| Binary.Length | 返回字符数。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binary-length) [英文](https://learn.microsoft.com/en-us/powerquery-m/binary-length) |
| Binary.Range | 返回以偏移量 binary 开头的二进制值的子集。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binary-range) [英文](https://learn.microsoft.com/en-us/powerquery-m/binary-range) |
| Binary.ToList | 将一个二进制值转换为一组数值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binary-tolist) [英文](https://learn.microsoft.com/en-us/powerquery-m/binary-tolist) |
| Binary.ToText | 返回将数字的二进制列表 binary 转换为文本值的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binary-totext) [英文](https://learn.microsoft.com/en-us/powerquery-m/binary-totext) |
| Binary.View | 返回 binary 的视图，向视图应用运算时，会使用 handlers 中指定的函数代替运算的默认行为。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binary-view) [英文](https://learn.microsoft.com/en-us/powerquery-m/binary-view) |
| Binary.ViewError | 根据 errorRecord 创建修改后的错误记录，该记录在视图上定义的处理程序引发时（通过 Binary.View）将不会触发回退。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binary-viewerror) [英文](https://learn.microsoft.com/en-us/powerquery-m/binary-viewerror) |
| Binary.ViewFunction | 基于 function 创建视图函数，此函数可以在 Binary.View 创建的视图中进行处理。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binary-viewfunction) [英文](https://learn.microsoft.com/en-us/powerquery-m/binary-viewfunction) |
| BinaryFormat.7BitEncodedSignedInteger | 一种二进制格式，读取使用 7 位可变长度编码进行编码的 64 位带符号整数。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binaryformat-7bitencodedsignedinteger) [英文](https://learn.microsoft.com/en-us/powerquery-m/binaryformat-7bitencodedsignedinteger) |
| BinaryFormat.7BitEncodedUnsignedInteger | 一种二进制格式，读取使用 7 位可变长度编码进行编码的 64 位无符号整数。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binaryformat-7bitencodedunsignedinteger) [英文](https://learn.microsoft.com/en-us/powerquery-m/binaryformat-7bitencodedunsignedinteger) |
| BinaryFormat.Binary | 返回读取二进制值的二进制格式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binaryformat-binary) [英文](https://learn.microsoft.com/en-us/powerquery-m/binaryformat-binary) |
| BinaryFormat.Byte | 读取 8 位无符号整数的二进制格式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binaryformat-byte) [英文](https://learn.microsoft.com/en-us/powerquery-m/binaryformat-byte) |
| BinaryFormat.ByteOrder | 以 binaryFormat 指定的字节顺序返回二进制格式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binaryformat-byteorder) [英文](https://learn.microsoft.com/en-us/powerquery-m/binaryformat-byteorder) |
| BinaryFormat.Choice | 返回一个二进制格式，它基于已读取的值选择下一个二进制格式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binaryformat-choice) [英文](https://learn.microsoft.com/en-us/powerquery-m/binaryformat-choice) |
| BinaryFormat.Decimal | 读取 .NET 16 字节十进制值的二进制格式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binaryformat-decimal) [英文](https://learn.microsoft.com/en-us/powerquery-m/binaryformat-decimal) |
| BinaryFormat.Double | 读取 8 字节 IEEE 双精度浮点值的二进制格式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binaryformat-double) [英文](https://learn.microsoft.com/en-us/powerquery-m/binaryformat-double) |
| BinaryFormat.Group | 参数如下： binaryFormat 参数指定键值的二进制格式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binaryformat-group) [英文](https://learn.microsoft.com/en-us/powerquery-m/binaryformat-group) |
| BinaryFormat.Length | 返回一个二进制格式，它限制可读取的数据量。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binaryformat-length) [英文](https://learn.microsoft.com/en-us/powerquery-m/binaryformat-length) |
| BinaryFormat.List | 返回可读取项序列的二进制格式并且返回一个 list。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binaryformat-list) [英文](https://learn.microsoft.com/en-us/powerquery-m/binaryformat-list) |
| BinaryFormat.Null | 读取零字节并且返回 NULL 的二进制格式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binaryformat-null) [英文](https://learn.microsoft.com/en-us/powerquery-m/binaryformat-null) |
| BinaryFormat.Record | 返回读取记录的二进制格式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binaryformat-record) [英文](https://learn.microsoft.com/en-us/powerquery-m/binaryformat-record) |
| BinaryFormat.SignedInteger16 | 读取 16 位带符号整数的二进制格式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binaryformat-signedinteger16) [英文](https://learn.microsoft.com/en-us/powerquery-m/binaryformat-signedinteger16) |
| BinaryFormat.SignedInteger32 | 读取 32 位带符号整数的二进制格式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binaryformat-signedinteger32) [英文](https://learn.microsoft.com/en-us/powerquery-m/binaryformat-signedinteger32) |
| BinaryFormat.SignedInteger64 | 读取 64 位带符号整数的二进制格式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binaryformat-signedinteger64) [英文](https://learn.microsoft.com/en-us/powerquery-m/binaryformat-signedinteger64) |
| BinaryFormat.Single | 读取 4 字节 IEEE 单精度浮点值的二进制格式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binaryformat-single) [英文](https://learn.microsoft.com/en-us/powerquery-m/binaryformat-single) |
| BinaryFormat.Text | 返回读取文本值的二进制格式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binaryformat-text) [英文](https://learn.microsoft.com/en-us/powerquery-m/binaryformat-text) |
| BinaryFormat.Transform | 返回一个二进制格式，该二进制格式将转换由另一个二进制格式读取的值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binaryformat-transform) [英文](https://learn.microsoft.com/en-us/powerquery-m/binaryformat-transform) |
| BinaryFormat.UnsignedInteger16 | 读取 16 位无符号整数的二进制格式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binaryformat-unsignedinteger16) [英文](https://learn.microsoft.com/en-us/powerquery-m/binaryformat-unsignedinteger16) |
| BinaryFormat.UnsignedInteger32 | 读取 32 位无符号整数的二进制格式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binaryformat-unsignedinteger32) [英文](https://learn.microsoft.com/en-us/powerquery-m/binaryformat-unsignedinteger32) |
| BinaryFormat.UnsignedInteger64 | 读取 64 位无符号整数的二进制格式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/binaryformat-unsignedinteger64) [英文](https://learn.microsoft.com/en-us/powerquery-m/binaryformat-unsignedinteger64) |
| #binary | 从数字列表或一个 Base 64 编码文本值创建一个二进制值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/sharpbinary) [英文](https://learn.microsoft.com/en-us/powerquery-m/sharpbinary) |
<h2 id='4'>4、合并器函数</h2>
<a href='#content'>返回目录</a>
| 函数名称 | 描述 | 链接 |
| :--: | :--: |:--: |
| Combiner.CombineTextByDelimiter | 返回一个函数，它使用指定的分隔符将文本列表合并成单个文本。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/combiner-combinetextbydelimiter) [英文](https://learn.microsoft.com/en-us/powerquery-m/combiner-combinetextbydelimiter) |
| Combiner.CombineTextByEachDelimiter | 返回一个函数，它按顺序使用每个指定的分隔符将文本列表合并成单个文本。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/combiner-combinetextbyeachdelimiter) [英文](https://learn.microsoft.com/en-us/powerquery-m/combiner-combinetextbyeachdelimiter) |
| Combiner.CombineTextByLengths | 返回一个函数，它使用指定的长度将文本列表合并成单个文本。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/combiner-combinetextbylengths) [英文](https://learn.microsoft.com/en-us/powerquery-m/combiner-combinetextbylengths) |
| Combiner.CombineTextByPositions | 返回一个函数，它使用指定的位置将文本列表合并成单个文本。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/combiner-combinetextbypositions) [英文](https://learn.microsoft.com/en-us/powerquery-m/combiner-combinetextbypositions) |
| Combiner.CombineTextByRanges | 返回一个函数，它使用指定的位置和长度将文本列表合并成单个文本。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/combiner-combinetextbyranges) [英文](https://learn.microsoft.com/en-us/powerquery-m/combiner-combinetextbyranges) |
<h2 id='5'>5、比较器函数</h2>
<a href='#content'>返回目录</a>
| 函数名称 | 描述 | 链接 |
| :--: | :--: |:--: |
| Comparer.Equals | 使用提供的 comparer，在对两个给定值（x 和 y）进行同等性检查的基础上返回一个 logical 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/comparer-equals) [英文](https://learn.microsoft.com/en-us/powerquery-m/comparer-equals) |
| Comparer.FromCulture | 返回一个比较器函数，得出用于比较的区分大小写的 culture 和逻辑值 ignoreCase。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/comparer-fromculture) [英文](https://learn.microsoft.com/en-us/powerquery-m/comparer-fromculture) |
| Comparer.Ordinal | 返回使用 Ordinal 规则来比较提供的值 x 和 y 的比较器函数。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/comparer-ordinal) [英文](https://learn.microsoft.com/en-us/powerquery-m/comparer-ordinal) |
| Comparer.OrdinalIgnoreCase | 返回使用 Ordinal 规则来比较提供的值 x 和 y 的不区分大小写的比较器函数。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/comparer-ordinalignorecase) [英文](https://learn.microsoft.com/en-us/powerquery-m/comparer-ordinalignorecase) |
<h2 id='6'>6、日期函数</h2>
<a href='#content'>返回目录</a>
| 函数名称 | 描述 | 链接 |
| :--: | :--: |:--: |
| Date.AddDays | 返回将 numberOfDays 天数添加到 datetime 值 dateTime 所得到的 date、datetime 或 datetimezone 结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-adddays) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-adddays) |
| Date.AddMonths | 返回将 numberOfMonths 月份添加到 datetime 值 dateTime 所得到的 date、datetime 或 datetimezone 结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-addmonths) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-addmonths) |
| Date.AddQuarters | 返回将 numberOfQuarters 个季度添加到 datetime 值 dateTime 所得到的 date、datetime 或 datetimezone 结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-addquarters) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-addquarters) |
| Date.AddWeeks | 返回向 datetime 值 dateTime 添加 numberOfWeeks 周后所得的 date、datetime 或 datetimezone 结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-addweeks) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-addweeks) |
| Date.AddYears | 返回将 numberOfYears 加上 datetime 值 dateTime 的 date、datetime 或 datetimezone 结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-addyears) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-addyears) |
| Date.Day | 返回 date、datetime 或 datetimezone 值的天数部分。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-day) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-day) |
| Date.DayOfWeek | 返回数字（介于 0 到 6 之间），以指明提供的 dateTime 是星期几。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-dayofweek) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-dayofweek) |
| Date.DayOfWeekName | 返回所提供的 date 是星期几。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-dayofweekname) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-dayofweekname) |
| Date.DayOfYear | 返回一个数字，代表所提供的 date、datetime 或 datetimezone 值 dateTime 中的一年中的某一天。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-dayofyear) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-dayofyear) |
| Date.DaysInMonth | 返回 date、datetime 或 datetimezone 值 dateTime 中月份的天数。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-daysinmonth) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-daysinmonth) |
| Date.EndOfDay | 返回由 dateTime 表示的天结束值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-endofday) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-endofday) |
| Date.EndOfMonth | 返回包含 dateTime 的月份结束值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-endofmonth) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-endofmonth) |
| Date.EndOfQuarter | 返回包含 dateTime 的季度结束值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-endofquarter) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-endofquarter) |
| Date.EndOfWeek | 返回包含 dateTime 的周结束值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-endofweek) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-endofweek) |
| Date.EndOfYear | 返回包含 dateTime 的年份结束值，包括分数秒。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-endofyear) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-endofyear) |
| Date.From | 从给定的 value 返回 date 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-from) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-from) |
| Date.FromText | 从文本表示形式 text 创建一个 date 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-fromtext) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-fromtext) |
| Date.IsInCurrentDay | 指示给定的日期/时间值 dateTime 是否按系统当前日期和时间所确定的那样处于当日内。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-isincurrentday) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-isincurrentday) |
| Date.IsInCurrentMonth | 指示给定的日期/时间值 dateTime 是否为当前这一个月的时间（由系统上的当前日期和时间确定）。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-isincurrentmonth) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-isincurrentmonth) |
| Date.IsInCurrentQuarter | 指示给定的日期时间值 dateTime 是否按系统当前日期和时间所确定的那样处于当季度内。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-isincurrentquarter) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-isincurrentquarter) |
| Date.IsInCurrentWeek | 指示给定的日期/时间值 dateTime 是否按系统当前日期和时间所确定的那样处于当周内。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-isincurrentweek) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-isincurrentweek) |
| Date.IsInCurrentYear | 指示给定的日期/时间值 dateTime 是否按系统当前日期和时间所确定的那样处于当前年份内。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-isincurrentyear) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-isincurrentyear) |
| Date.IsInNextDay | 指示给定的日期时间值 dateTime 是否按系统当前日期和时间所确定的那样处于下一天内。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-isinnextday) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-isinnextday) |
| Date.IsInNextMonth | 指示给定的日期/时间值 dateTime 是否按系统当前日期和时间所确定的那样处于下一月内。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-isinnextmonth) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-isinnextmonth) |
| Date.IsInNextNDays | 指示给定的日期时间值 dateTime 是否按系统当前日期和时间所确定的那样处于接下来的天数内。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-isinnextndays) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-isinnextndays) |
| Date.IsInNextNMonths | 指示给定的日期时间值 dateTime 是否按系统当前日期和时间所确定的那样处于接下来的月份数内。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-isinnextnmonths) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-isinnextnmonths) |
| Date.IsInNextNQuarters | 指示给定的日期/时间值 dateTime 是否按系统当前日期和时间所确定的那样处于下一季度数内。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-isinnextnquarters) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-isinnextnquarters) |
| Date.IsInNextNWeeks | 指示给定的日期/时间值 dateTime 是否为下几周的时间（由系统上的当前日期和时间确定）。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-isinnextnweeks) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-isinnextnweeks) |
| Date.IsInNextNYears | 指示给定的日期/时间值 dateTime 是否为下几年的时间（由系统上的当前日期和时间确定）。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-isinnextnyears) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-isinnextnyears) |
| Date.IsInNextQuarter | 指示给定的日期时间值 dateTime 是否按系统当前日期和时间所确定的那样处于下季度内。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-isinnextquarter) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-isinnextquarter) |
| Date.IsInNextWeek | 指示给定的日期/时间值 (dateTime) 是否为下周的时间（由系统上的当前日期和时间确定）。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-isinnextweek) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-isinnextweek) |
| Date.IsInNextYear | 指示给定的日期/时间值 dateTime 是否按系统当前日期和时间所确定的那样处于下一年份内。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-isinnextyear) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-isinnextyear) |
| Date.IsInPreviousDay | 指示给定的日期/时间值 dateTime 是否按系统当前日期和时间所确定的那样处于前一天内。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-isinpreviousday) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-isinpreviousday) |
| Date.IsInPreviousMonth | 指示给定的日期/时间值 dateTime 是否按系统当前日期和时间所确定的那样处于上一月内。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-isinpreviousmonth) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-isinpreviousmonth) |
| Date.IsInPreviousNDays | 指示给定的日期/时间值 dateTime 是否按系统当前日期和时间所确定的那样处于之前的天数内。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-isinpreviousndays) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-isinpreviousndays) |
| Date.IsInPreviousNMonths | 指示给定的日期时间值 dateTime 是否按系统当前日期和时间所确定的那样处于之前的月份数内。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-isinpreviousnmonths) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-isinpreviousnmonths) |
| Date.IsInPreviousNQuarters | 指示给定的日期/时间值 dateTime 是否为前几个季度的时间（由系统上的当前日期和时间确定）。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-isinpreviousnquarters) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-isinpreviousnquarters) |
| Date.IsInPreviousNWeeks | 指示给定的日期/时间值 dateTime 是否为前几周的时间（由系统上的当前日期和时间确定）。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-isinpreviousnweeks) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-isinpreviousnweeks) |
| Date.IsInPreviousNYears | 指示给定的日期/时间值 dateTime 是否按系统当前日期和时间所确定的那样处于之前的年数内。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-isinpreviousnyears) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-isinpreviousnyears) |
| Date.IsInPreviousQuarter | 指示给定的日期/时间值 dateTime 是否按系统当前日期和时间所确定的那样处于上一季度内。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-isinpreviousquarter) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-isinpreviousquarter) |
| Date.IsInPreviousWeek | 指示给定的日期时间值 dateTime 是否按系统当前日期和时间所确定的那样处于上一周内。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-isinpreviousweek) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-isinpreviousweek) |
| Date.IsInPreviousYear | 指示给定的日期/时间值 dateTime 是否按系统当前日期和时间所确定的那样处于上一年份内。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-isinpreviousyear) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-isinpreviousyear) |
| Date.IsInYearToDate | 指示在当前年份中该给定日期值 dateTime 是否出现以及该日期是否就在当天或早于当天，它由系统上的当前日期和时间确定。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-isinyeartodate) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-isinyeartodate) |
| Date.IsLeapYear | 指示给定的日期/时间值 dateTime 是否处于闰年中。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-isleapyear) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-isleapyear) |
| Date.Month | 返回所提供的 datetime 值的月份部分 dateTime。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-month) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-month) |
| Date.MonthName | 返回所提供 date 的月份部分的名称。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-monthname) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-monthname) |
| Date.QuarterOfYear | 返回一个介于 1 到 4 之间的数值，该数值指示日期 dateTime 属于年份中的哪一季度。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-quarterofyear) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-quarterofyear) |
| Date.StartOfDay | 返回由 dateTime 表示的天开始值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-startofday) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-startofday) |
| Date.StartOfMonth | 返回包含 dateTime 的月份开始值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-startofmonth) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-startofmonth) |
| Date.StartOfQuarter | 返回包含 dateTime 的季度开始值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-startofquarter) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-startofquarter) |
| Date.StartOfWeek | 返回包含 dateTime 的周开始值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-startofweek) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-startofweek) |
| Date.StartOfYear | 返回包含 dateTime 的年份的开始值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-startofyear) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-startofyear) |
| Date.ToRecord | 返回包含给定日期值 date 的各个部分的记录。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-torecord) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-torecord) |
| Date.ToText | 返回 date 的文本化表示形式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-totext) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-totext) |
| Date.WeekOfMonth | 返回一个介于 1 到 6 之间的数值，该数值指示日期 dateTime 属于月份中的哪一周。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-weekofmonth) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-weekofmonth) |
| Date.WeekOfYear | 返回一个介于 1 到 54 之间的数值，该数值指示日期 dateTime 属于年份中的哪一周。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-weekofyear) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-weekofyear) |
| Date.Year | 返回所提供的 datetime 值 dateTime 的年份部分。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/date-year) [英文](https://learn.microsoft.com/en-us/powerquery-m/date-year) |
| #date | 从表示年、月和日的整数创建日期值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/sharpdate) [英文](https://learn.microsoft.com/en-us/powerquery-m/sharpdate) |
<h2 id='7'>7、日期/时间函数</h2>
<a href='#content'>返回目录</a>
| 函数名称 | 描述 | 链接 |
| :--: | :--: |:--: |
| DateTime.AddZone | 将时区信息添加到 dateTime 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetime-addzone) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetime-addzone) |
| DateTime.Date | 返回给定的 date、datetime 或 datetimezone 值 dateTime 的日期部分。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetime-date) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetime-date) |
| DateTime.FixedLocalNow | 返回设置为系统上的当前日期和时间的 datetime 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetime-fixedlocalnow) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetime-fixedlocalnow) |
| DateTime.From | 从给定的 value 返回 datetime 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetime-from) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetime-from) |
| DateTime.FromFileTime | 根据 fileTime 值创建 datetime 值，并将其转换为本地时区。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetime-fromfiletime) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetime-fromfiletime) |
| DateTime.FromText | 从文本表示形式 text 创建一个 datetime 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetime-fromtext) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetime-fromtext) |
| DateTime.IsInCurrentHour | 指示给定的日期/时间值 dateTime 是否为当前这一小时的时间（由系统上的当前日期和时间确定）。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetime-isincurrenthour) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetime-isincurrenthour) |
| DateTime.IsInCurrentMinute | 指示给定的日期/时间值 dateTime 是否为当前这一分钟的时间（由系统上的当前日期和时间确定）。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetime-isincurrentminute) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetime-isincurrentminute) |
| DateTime.IsInCurrentSecond | 指示给定的日期/时间值 dateTime 是否为当前这一秒的时间（由系统上的当前日期和时间确定）。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetime-isincurrentsecond) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetime-isincurrentsecond) |
| DateTime.IsInNextHour | 指示给定的日期时间值（dateTime）是否按系统当前日期和时间所确定的那样处于下一小时内。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetime-isinnexthour) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetime-isinnexthour) |
| DateTime.IsInNextMinute | 指示给定的日期/时间值 dateTime 是否处于下一分钟内（由系统上的当前日期和时间确定）。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetime-isinnextminute) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetime-isinnextminute) |
| DateTime.IsInNextNHours | 指示给定的日期/时间值 dateTime 是否处于接下来的几小时时间内（由系统上的当前日期和时间确定）。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetime-isinnextnhours) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetime-isinnextnhours) |
| DateTime.IsInNextNMinutes | 指示给定的日期时间值 dateTime 是否按系统当前日期和时间所确定的那样处于接下来的分钟数内。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetime-isinnextnminutes) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetime-isinnextnminutes) |
| DateTime.IsInNextNSeconds | 指示给定的日期/时间值 dateTime 是否为下几秒的时间（由系统上的当前日期和时间确定）。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetime-isinnextnseconds) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetime-isinnextnseconds) |
| DateTime.IsInNextSecond | 指示给定的日期/时间值 (dateTime) 是否为下一秒的时间（由系统上的当前日期和时间确定）。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetime-isinnextsecond) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetime-isinnextsecond) |
| DateTime.IsInPreviousHour | 指示给定的日期/时间值 dateTime 是否为上一小时的时间（由系统上的当前日期和时间确定）。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetime-isinprevioushour) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetime-isinprevioushour) |
| DateTime.IsInPreviousMinute | 指示给定的日期/时间值 dateTime 是否按系统当前日期和时间所确定的那样处于上一分钟内。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetime-isinpreviousminute) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetime-isinpreviousminute) |
| DateTime.IsInPreviousNHours | 指示给定的日期/时间值 dateTime 是否按系统当前日期和时间所确定的那样处于之前的小时数内。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetime-isinpreviousnhours) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetime-isinpreviousnhours) |
| DateTime.IsInPreviousNMinutes | 指示给定的日期/时间值 dateTime 是否按系统当前日期和时间所确定的那样处于之前的分钟数内。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetime-isinpreviousnminutes) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetime-isinpreviousnminutes) |
| DateTime.IsInPreviousNSeconds | 指示给定的日期/时间值 dateTime 是否按系统当前日期和时间所确定的那样处于之前的秒数内。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetime-isinpreviousnseconds) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetime-isinpreviousnseconds) |
| DateTime.IsInPreviousSecond | 指示给定的日期/时间值 dateTime 是否处于前一秒内（由系统上的当前日期和时间确定）。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetime-isinprevioussecond) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetime-isinprevioussecond) |
| DateTime.LocalNow | 返回设置为系统上的当前日期和时间的 datetime 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetime-localnow) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetime-localnow) |
| DateTime.Time | 返回给定日期/时间值 dateTime 的时间部分。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetime-time) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetime-time) |
| DateTime.ToRecord | 返回包含给定日期/时间值 dateTime 的各个部分的记录。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetime-torecord) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetime-torecord) |
| DateTime.ToText | 返回 dateTime 的文本化表示形式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetime-totext) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetime-totext) |
| #datetime | 从表示年、月、日、小时、分钟和（小数）秒的数值创建 datetime 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/sharpdatetime) [英文](https://learn.microsoft.com/en-us/powerquery-m/sharpdatetime) |
<h2 id='8'>8、日期/时间/时区函数</h2>
<a href='#content'>返回目录</a>
| 函数名称 | 描述 | 链接 |
| :--: | :--: |:--: |
| DateTimeZone.FixedLocalNow | 返回设置为系统上的当前日期和时间的 datetime 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetimezone-fixedlocalnow) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetimezone-fixedlocalnow) |
| DateTimeZone.FixedUtcNow | 返回采用 UTC（GMT 时区）表示的当前日期和时间。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetimezone-fixedutcnow) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetimezone-fixedutcnow) |
| DateTimeZone.From | 从给定的 value 返回 datetimezone 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetimezone-from) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetimezone-from) |
| DateTimeZone.FromFileTime | 根据 fileTime 值创建 datetimezone 值，并将其转换为本地时区。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetimezone-fromfiletime) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetimezone-fromfiletime) |
| DateTimeZone.FromText | 从文本表示形式 text 创建一个 datetimezone 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetimezone-fromtext) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetimezone-fromtext) |
| DateTimeZone.LocalNow | 返回设置为系统上的当前日期和时间的 datetimezone 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetimezone-localnow) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetimezone-localnow) |
| DateTimeZone.RemoveZone | 从 dateTimeZone 返回 #datetime 值并删除其中的时区信息。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetimezone-removezone) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetimezone-removezone) |
| DateTimeZone.SwitchZone | 将 datetimezone 值 dateTimeZone 的时区信息更改为 timezoneHours 和 timezoneMinutes（可选）提供的新时区信息。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetimezone-switchzone) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetimezone-switchzone) |
| DateTimeZone.ToLocal | 将 datetimezone 值 dateTimeZone 的时区信息更改为本地时区信息。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetimezone-tolocal) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetimezone-tolocal) |
| DateTimeZone.ToRecord | 返回包含给定 datetimezone 值 dateTimeZone 的各个部分的记录。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetimezone-torecord) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetimezone-torecord) |
| DateTimeZone.ToText | 返回 dateTimeZone 的文本化表示形式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetimezone-totext) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetimezone-totext) |
| DateTimeZone.ToUtc | 将日期时间值 dateTimeZone 的时区信息更改为 UTC 或通用时间时区信息。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetimezone-toutc) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetimezone-toutc) |
| DateTimeZone.UtcNow | 返回采用 UTC（GMT 时区）表示的当前日期和时间。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetimezone-utcnow) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetimezone-utcnow) |
| DateTimeZone.ZoneHours | 更改值的时区。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetimezone-zonehours) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetimezone-zonehours) |
| DateTimeZone.ZoneMinutes | 更改值的时区。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/datetimezone-zoneminutes) [英文](https://learn.microsoft.com/en-us/powerquery-m/datetimezone-zoneminutes) |
| #datetimezone | 从表示年、月、日、小时、分钟、（小数）秒、（小数）偏移小时，以及偏移分钟的数值创建 datetimezone 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/sharpdatetimezone) [英文](https://learn.microsoft.com/en-us/powerquery-m/sharpdatetimezone) |
<h2 id='9'>9、持续时间函数</h2>
<a href='#content'>返回目录</a>
| 函数名称 | 描述 | 链接 |
| :--: | :--: |:--: |
| Duration.Days | 返回 duration 的天数部分。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/duration-days) [英文](https://learn.microsoft.com/en-us/powerquery-m/duration-days) |
| Duration.From | 从给定的 value 返回 duration 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/duration-from) [英文](https://learn.microsoft.com/en-us/powerquery-m/duration-from) |
| Duration.FromText | 从指定的文本 text 返回持续时间值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/duration-fromtext) [英文](https://learn.microsoft.com/en-us/powerquery-m/duration-fromtext) |
| Duration.Hours | 返回 duration 的小时数部分。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/duration-hours) [英文](https://learn.microsoft.com/en-us/powerquery-m/duration-hours) |
| Duration.Minutes | 返回 duration 的分钟数部分。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/duration-minutes) [英文](https://learn.microsoft.com/en-us/powerquery-m/duration-minutes) |
| Duration.Seconds | 返回 duration 的秒数部分。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/duration-seconds) [英文](https://learn.microsoft.com/en-us/powerquery-m/duration-seconds) |
| Duration.ToRecord | 返回包含持续时间值 duration 的各个部分的记录。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/duration-torecord) [英文](https://learn.microsoft.com/en-us/powerquery-m/duration-torecord) |
| Duration.TotalDays | 返回 duration 跨越的总天数。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/duration-totaldays) [英文](https://learn.microsoft.com/en-us/powerquery-m/duration-totaldays) |
| Duration.TotalHours | 返回 duration 跨越的总小时数。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/duration-totalhours) [英文](https://learn.microsoft.com/en-us/powerquery-m/duration-totalhours) |
| Duration.TotalMinutes | 返回 duration 跨越的总分钟数。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/duration-totalminutes) [英文](https://learn.microsoft.com/en-us/powerquery-m/duration-totalminutes) |
| Duration.TotalSeconds | 返回 duration 跨越的总秒数。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/duration-totalseconds) [英文](https://learn.microsoft.com/en-us/powerquery-m/duration-totalseconds) |
| Duration.ToText | 以 "day.hour:mins:sec" 格式返回给定持续时间值 duration 的文本表示形式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/duration-totext) [英文](https://learn.microsoft.com/en-us/powerquery-m/duration-totext) |
| #duration | 从表示天、小时、分钟和（小数）秒的数值创建持续时间值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/sharpduration) [英文](https://learn.microsoft.com/en-us/powerquery-m/sharpduration) |
<h2 id='10'>10、错误处理函数</h2>
<a href='#content'>返回目录</a>
| 函数名称 | 描述 | 链接 |
| :--: | :--: |:--: |
| Diagnostics.ActivityId | 为当前正在运行的计算返回不透明的标识符。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/diagnostics-activityid) [英文](https://learn.microsoft.com/en-us/powerquery-m/diagnostics-activityid) |
| Diagnostics.Trace | 写入跟踪 message（如果已启用跟踪的话）并返回 value。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/diagnostics-trace) [英文](https://learn.microsoft.com/en-us/powerquery-m/diagnostics-trace) |
| Error.Record | 从为原因、消息和详细信息提供的文本值返回错误记录。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/error-record) [英文](https://learn.microsoft.com/en-us/powerquery-m/error-record) |
<h2 id='11'>11、表达式函数</h2>
<a href='#content'>返回目录</a>
| 函数名称 | 描述 | 链接 |
| :--: | :--: |:--: |
| Expression.Constant | 返回常数值的 M 源代码表示形式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/expression-constant) [英文](https://learn.microsoft.com/en-us/powerquery-m/expression-constant) |
| Expression.Evaluate | 返回 M 表达式 document 的计算结果，其中可用的标识符可以由 environment 进行引用和定义。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/expression-evaluate) [英文](https://learn.microsoft.com/en-us/powerquery-m/expression-evaluate) |
| Expression.Identifier | 返回标识符 name 的 M 源代码表示形式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/expression-identifier) [英文](https://learn.microsoft.com/en-us/powerquery-m/expression-identifier) |
<h2 id='12'>12、函数值</h2>
<a href='#content'>返回目录</a>
| 函数名称 | 描述 | 链接 |
| :--: | :--: |:--: |
| Function.From | 采用一元函数 function 并创建一个类型为 functionType 的新函数，用于构造其参数列表，并将其传递给 function。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/function-from) [英文](https://learn.microsoft.com/en-us/powerquery-m/function-from) |
| Function.Invoke | 使用指定的参数列表调用给定的函数并返回结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/function-invoke) [英文](https://learn.microsoft.com/en-us/powerquery-m/function-invoke) |
| Function.InvokeAfter | 经过持续时间 delay 后，返回调用 function 的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/function-invokeafter) [英文](https://learn.microsoft.com/en-us/powerquery-m/function-invokeafter) |
| Function.IsDataSource | 返回是否将 function 视为数据源。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/function-isdatasource) [英文](https://learn.microsoft.com/en-us/powerquery-m/function-isdatasource) |
| Function.ScalarVector | 返回 scalarFunctionType 类型的标量函数，该函数使用单行参数调用 vectorFunction 并返回其单个输出。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/function-scalarvector) [英文](https://learn.microsoft.com/en-us/powerquery-m/function-scalarvector) |
<h2 id='13'>13、行函数</h2>
<a href='#content'>返回目录</a>
| 函数名称 | 描述 | 链接 |
| :--: | :--: |:--: |
| Lines.FromBinary | 将二进制值转换为在换行符处拆分的文本值列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/lines-frombinary) [英文](https://learn.microsoft.com/en-us/powerquery-m/lines-frombinary) |
| Lines.FromText | 将文本值转换为在换行符处拆分的文本值列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/lines-fromtext) [英文](https://learn.microsoft.com/en-us/powerquery-m/lines-fromtext) |
| Lines.ToBinary | 使用指定的编码和 lineSeparator 将文本列表转换为二进制值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/lines-tobinary) [英文](https://learn.microsoft.com/en-us/powerquery-m/lines-tobinary) |
| Lines.ToText | 将文本列表转换成单个文本。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/lines-totext) [英文](https://learn.microsoft.com/en-us/powerquery-m/lines-totext) |
<h2 id='14'>14、列表函数</h2>
<a href='#content'>返回目录</a>
| 函数名称 | 描述 | 链接 |
| :--: | :--: |:--: |
| List.Accumulate | 使用 accumulator 从列表 list 中的项累积汇总值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-accumulate) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-accumulate) |
| List.AllTrue | 如果列表 list 中的所有表达式均为 true，则返回 true。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-alltrue) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-alltrue) |
| List.Alternate | 返回由列表中所有奇数编号的偏移元素组成的列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-alternate) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-alternate) |
| List.AnyTrue | 如果列表 list 中的任意表达式为 true，则返回 true。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-anytrue) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-anytrue) |
| List.Average | 返回列表 list 中项的平均值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-average) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-average) |
| List.Buffer | 在内存中缓冲列表 list。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-buffer) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-buffer) |
| List.Combine | 获取一系列的列表 lists 并将它们合并为一个新列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-combine) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-combine) |
| List.ConformToPageReader | 此函数仅计划供内部使用。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-conformtopagereader) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-conformtopagereader) |
| List.Contains | 指示列表 list 是否包含值 value。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-contains) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-contains) |
| List.ContainsAll | 指示列表 list 是否包含另一个列表中的所有值 values。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-containsall) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-containsall) |
| List.ContainsAny | 指示一个列表 list 是否包含另一个列表中的任意值 values。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-containsany) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-containsany) |
| List.Count | 返回列表 list 中的项数。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-count) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-count) |
| List.Covariance | 返回两个列表（numberList1 和 numberList2）之间的协方差。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-covariance) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-covariance) |
| List.Dates | 从 start 开始，返回大小为 count 的 date 值的列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-dates) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-dates) |
| List.DateTimes | 从 start 开始，返回大小为 count 的 datetime 值的列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-datetimes) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-datetimes) |
| List.DateTimeZones | 从 start 开始，返回大小为 count 的 datetimezone 值的列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-datetimezones) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-datetimezones) |
| List.Difference | 返回列表 list1 中未出现在列表 list2 中的项。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-difference) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-difference) |
| List.Distinct | 返回一个列表，此列表包含列表 list 中的所有值，并且表中重复项已被删除。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-distinct) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-distinct) |
| List.Durations | 返回 countduration 值的列表，从 start 开始，并按给定的 durationstep 递增。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-durations) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-durations) |
| List.FindText | 从包含值 text 的列表 list 返回值列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-findtext) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-findtext) |
| List.First | 返回 list 列表中的第一项；如果列表为空，则返回可选默认值 defaultValue。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-first) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-first) |
| List.FirstN | 在列表 {3, 4, 5, -1, 7, 8, 2} 中查找大于 0 的初始值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-firstn) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-firstn) |
| List.Generate | 使用提供的函数生成值列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-generate) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-generate) |
| List.InsertRange | 返回新列表，该列表是通过将 values 中的值插入到 index 中的 list 而生成的。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-insertrange) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-insertrange) |
| List.Intersect | 返回在输入列表 lists 中找到的列表值的交集。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-intersect) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-intersect) |
| List.IsDistinct | 返回一个逻辑值，指示列表 list 中是否有重复值；如果列表是非重复的，则为 true，否则为 false。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-isdistinct) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-isdistinct) |
| List.IsEmpty | 如果列表 list不包含任何值（长度为 0），则返回 true。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-isempty) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-isempty) |
| List.Last | 返回 list 列表的最后一项，如果列表为空，则返回可选默认值 defaultValue。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-last) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-last) |
| List.LastN | 返回列表 list 中的最后一项。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-lastn) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-lastn) |
| List.MatchesAll | 如果列表 list 中的所有值均满足条件函数 condition，则返回 true，否则返回 false。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-matchesall) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-matchesall) |
| List.MatchesAny | 如果列表 list 中的任何值满足条件函数 condition，则返回 true否则返回 false。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-matchesany) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-matchesany) |
| List.Max | 返回 list 列表中最大的一项；如果列表为空，则返回可选默认值 default。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-max) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-max) |
| List.MaxN | 返回列表 list 中的最大值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-maxn) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-maxn) |
| List.Median | 返回列表 list 的中值项。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-median) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-median) |
| List.Min | 返回 list 列表中最小的一项；如果列表为空，则返回可选默认值 default。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-min) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-min) |
| List.MinN | 返回列表 list 中的最小值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-minn) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-minn) |
| List.Mode | 返回 list 中出现最频繁的项。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-mode) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-mode) |
| List.Modes | 返回 list 中出现频率最高的项目。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-modes) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-modes) |
| List.NonNullCount | 返回列表 list 中的非 NULL 项数。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-nonnullcount) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-nonnullcount) |
| List.Numbers | 返回给定了初始值、计数和可选增量值的数值列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-numbers) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-numbers) |
| List.Percentile | 返回 list 列表的一个或多个示例百分位数。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-percentile) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-percentile) |
| List.PositionOf | 返回 value 值在列表 list 中显示的值的偏移量。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-positionof) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-positionof) |
| List.PositionOfAny | 返回列表 values 中的值第一次出现的列表 list 中的偏移值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-positionofany) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-positionofany) |
| List.Positions | 返回 list 输入列表的偏移量列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-positions) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-positions) |
| List.Product | 返回列表 numbersList 中非 NULL 数的乘积。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-product) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-product) |
| List.Random | 给定要生成的值数量和可选种子值，返回介于 0 到 1 之间的随机数的列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-random) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-random) |
| List.Range | 返回从偏移量开始的列表 list 的子集。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-range) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-range) |
| List.RemoveFirstN | 返回一个列表，该列表删除列表 list 的第一个元素。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-removefirstn) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-removefirstn) |
| List.RemoveItems | 从 list1 中删除在 list2 中出现的所有给定值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-removeitems) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-removeitems) |
| List.RemoveLastN | 返回一个列表，它从列表 list 末尾删除最后几个 countOrCondition 元素。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-removelastn) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-removelastn) |
| List.RemoveMatchingItems | 从列表 list1 删除 list2 中出现的所有给定值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-removematchingitems) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-removematchingitems) |
| List.RemoveNulls | 删除 list 中出现的所有“NULL”值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-removenulls) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-removenulls) |
| List.RemoveRange | 在 list 中删除从指定位置 index 起的 count 个值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-removerange) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-removerange) |
| List.Repeat | 返回为原始列表 list 的 count 次重复的列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-repeat) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-repeat) |
| List.ReplaceMatchingItems | 对列表 list 执行给定的替换。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-replacematchingitems) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-replacematchingitems) |
| List.ReplaceRange | 从指定的位置 index 开始，使用列表 replaceWith 替换 list 中的 count 个值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-replacerange) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-replacerange) |
| List.ReplaceValue | 在值列表 list 中搜索值 oldValue，每次找到后使用替换值 newValue 将其替换。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-replacevalue) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-replacevalue) |
| List.Reverse | 返回将列表 list 中的值反向排序得到的列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-reverse) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-reverse) |
| List.Select | 从列表 list 返回匹配选择条件 selection 的值的列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-select) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-select) |
| List.Single | 如果列表 list 中只有一个项，则返回该项。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-single) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-single) |
| List.SingleOrDefault | 如果列表 list 中只有一个项，则返回该项。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-singleordefault) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-singleordefault) |
| List.Skip | 返回一个列表，此列表跳过列表 list 的第一个元素。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-skip) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-skip) |
| List.Sort | 根据指定的可选条件对数据列表 list 排序。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-sort) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-sort) |
| List.Split | 将 list 拆分为一系列列表，其中输出列表的第一个元素是包含源列表中前 pageSize 个元素的列表，输出列表的下一个元素是包含源列表中接下来 pageSize 个元素的列表，以此类推。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-split) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-split) |
| List.StandardDeviation | 返回列表 numbersList 中值的标准偏差的基于样本估计值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-standarddeviation) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-standarddeviation) |
| List.Sum | 返回列表（list）中非 NULL 值的总和。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-sum) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-sum) |
| List.Times | 从 start 开始，返回大小为 count 的 time 值的列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-times) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-times) |
| List.Transform | 通过将转换函数 transform 应用到列表 list 来返回值的新列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-transform) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-transform) |
| List.TransformMany | 返回一个列表，其元素是基于输入列表投射而来的。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-transformmany) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-transformmany) |
| List.Union | 采用列表 lists 的列表，联合各个列表中的项，并在输出列表中返回这些项。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-union) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-union) |
| List.Zip | 提取列表 lists 的其中一个列表，并返回一个列表显示在同一位置合并项的列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/list-zip) [英文](https://learn.microsoft.com/en-us/powerquery-m/list-zip) |
<h2 id='15'>15、逻辑函数</h2>
<a href='#content'>返回目录</a>
| 函数名称 | 描述 | 链接 |
| :--: | :--: |:--: |
| Logical.From | 从给定的 value 返回 logical 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/logical-from) [英文](https://learn.microsoft.com/en-us/powerquery-m/logical-from) |
| Logical.FromText | 从文本值 text（“true”或“false”）创建逻辑值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/logical-fromtext) [英文](https://learn.microsoft.com/en-us/powerquery-m/logical-fromtext) |
| Logical.ToText | 从逻辑值 logicalValue（true 或 false）创建文本值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/logical-totext) [英文](https://learn.microsoft.com/en-us/powerquery-m/logical-totext) |
<h2 id='16'>16、数字函数</h2>
<a href='#content'>返回目录</a>
| 函数名称 | 描述 | 链接 |
| :--: | :--: |:--: |
| Byte.From | 从给定的 value 中返回 8 位整数 number 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/byte-from) [英文](https://learn.microsoft.com/en-us/powerquery-m/byte-from) |
| Currency.From | 从给定的 value 返回 currency 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/currency-from) [英文](https://learn.microsoft.com/en-us/powerquery-m/currency-from) |
| Decimal.From | 从给定的 value 返回十进制 number 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/decimal-from) [英文](https://learn.microsoft.com/en-us/powerquery-m/decimal-from) |
| Double.From | 从给定的 value 返回双精度 number 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/double-from) [英文](https://learn.microsoft.com/en-us/powerquery-m/double-from) |
| Int8.From | 从给定的 value 返回带符号的 8 位整数 number 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/int8-from) [英文](https://learn.microsoft.com/en-us/powerquery-m/int8-from) |
| Int16.From | 从给定的 value 返回 16 位整数 number 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/int16-from) [英文](https://learn.microsoft.com/en-us/powerquery-m/int16-from) |
| Int32.From | 从给定的 value 返回 32 位整数 number 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/int32-from) [英文](https://learn.microsoft.com/en-us/powerquery-m/int32-from) |
| Int64.From | 从给定的 value 返回 64 位整数 number 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/int64-from) [英文](https://learn.microsoft.com/en-us/powerquery-m/int64-from) |
| Number.Abs | 返回 number 的绝对值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-abs) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-abs) |
| Number.Acos | 返回 number 的反余弦。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-acos) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-acos) |
| Number.Asin | 返回 number 的反正弦。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-asin) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-asin) |
| Number.Atan | 返回 number 的反正切。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-atan) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-atan) |
| Number.Atan2 | 返回其正切为 y 和 x 这两个数字的商 y/x 的角度（以弧度为单位）。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-atan2) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-atan2) |
| Number.BitwiseAnd | 返回对 number1 和 number2 执行按位“And”运算所得的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-bitwiseand) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-bitwiseand) |
| Number.BitwiseNot | 返回对 number 执行按位“Not”运算所得的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-bitwisenot) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-bitwisenot) |
| Number.BitwiseOr | 返回对 number1 和 number2 执行按位“Or”所得的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-bitwiseor) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-bitwiseor) |
| Number.BitwiseShiftLeft | 返回对 number1 执行按位左移指定的位数 number2 所得的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-bitwiseshiftleft) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-bitwiseshiftleft) |
| Number.BitwiseShiftRight | 返回对 number1 执行按位右移指定的位数 number2 所得的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-bitwiseshiftright) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-bitwiseshiftright) |
| Number.BitwiseXor | 返回对 number1 和 number2 执行按位“XOR”（异或）所得的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-bitwisexor) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-bitwisexor) |
| Number.Combinations | 返回项列表 setSize 中具有指定组合大小 combinationSize 的唯一组合数。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-combinations) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-combinations) |
| Number.Cos | 返回 number 的余弦值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-cos) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-cos) |
| Number.Cosh | 返回 number 的双曲余弦。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-cosh) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-cosh) |
| Number.Exp | 返回计算 e 的 number 次幂（指数函数）所得的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-exp) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-exp) |
| Number.Factorial | 返回数 number 的阶乘。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-factorial) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-factorial) |
| Number.From | 从给定的 value 返回 number 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-from) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-from) |
| Number.FromText | 从给定的文本值 text 返回 number 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-fromtext) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-fromtext) |
| Number.IntegerDivide | 返回将数字 number1 除以另一个数字 number2 的结果的整数部分。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-integerdivide) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-integerdivide) |
| Number.IsEven | 通过返回 true（如果为偶数）或 false（不是偶数），来指示值 number 是否为偶数。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-iseven) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-iseven) |
| Number.IsNaN | 指示值是否为 NAN（不是数字）。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-isnan) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-isnan) |
| Number.IsOdd | 指示值是否为奇数。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-isodd) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-isodd) |
| Number.Ln | 返回某一数字 number 的自然对数 。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-ln) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-ln) |
| Number.Log | 返回数值 number 以指定的 base 为底的对数。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-log) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-log) |
| Number.Log10 | 返回数值 number 的以 10 为底的对数。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-log10) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-log10) |
| Number.Mod | 返回用 divisor 整除 number 所得的余数。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-mod) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-mod) |
| Number.Permutations | 使用指定的排列大小 permutationSize 返回可从项数 setSize 生成的排列数。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-permutations) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-permutations) |
| Number.Power | 返回将 number 提升为 power 的幂的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-power) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-power) |
| Number.Random | 返回介于 0 到 1 之间的随机数。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-random) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-random) |
| Number.RandomBetween | 返回介于 bottom 和 top 之间的随机数。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-randombetween) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-randombetween) |
| Number.Round | 返回将 number 舍入为最接近的数字的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-round) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-round) |
| Number.RoundAwayFromZero | 返回 number 基于数的正负的舍入结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-roundawayfromzero) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-roundawayfromzero) |
| Number.RoundDown | 返回将 number 向下舍入到上一个最大整数的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-rounddown) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-rounddown) |
| Number.RoundTowardZero | 返回 number 基于数的正负的舍入结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-roundtowardzero) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-roundtowardzero) |
| Number.RoundUp | 返回将 number 向上舍入到下一个最大整数的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-roundup) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-roundup) |
| Number.Sign | 如果 number 为正数，返回 1，如果为负数，返回 -1，如果为零，返回 0。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-sign) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-sign) |
| Number.Sin | 返回 number 的正弦值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-sin) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-sin) |
| Number.Sinh | 返回 number 的双曲正弦。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-sinh) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-sinh) |
| Number.Sqrt | 返回 number 的平方根。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-sqrt) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-sqrt) |
| Number.Tan | 返回 number 的正切。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-tan) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-tan) |
| Number.Tanh | 返回 number 的双曲正切值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-tanh) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-tanh) |
| Number.ToText | 根据 format 指定的格式，将数值 number 格式化为文本值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/number-totext) [英文](https://learn.microsoft.com/en-us/powerquery-m/number-totext) |
| Percentage.From | 从给定的 value 返回 percentage 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/percentage-from) [英文](https://learn.microsoft.com/en-us/powerquery-m/percentage-from) |
| Single.From | 从给定的 value 返回单精度 number 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/single-from) [英文](https://learn.microsoft.com/en-us/powerquery-m/single-from) |
<h2 id='17'>17、记录函数</h2>
<a href='#content'>返回目录</a>
| 函数名称 | 描述 | 链接 |
| :--: | :--: |:--: |
| Geography.FromWellKnownText | 将以已知文本 (WKT) 格式表示地理值的文本转换为结构化记录。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/geography-fromwellknowntext) [英文](https://learn.microsoft.com/en-us/powerquery-m/geography-fromwellknowntext) |
| Geography.ToWellKnownText | 将结构化地理点值转换为由开放地理空间信息联盟 (OGC) 定义的已知文本 (WKT) 表示形式，这种形式也是许多数据库（包括 SQL Server）使用的序列化格式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/geography-towellknowntext) [英文](https://learn.microsoft.com/en-us/powerquery-m/geography-towellknowntext) |
| GeographyPoint.From | 创建一个记录，该记录表示一个地理点的构成部分，例如经度、纬度，以及海拔和度量值 (M)（如果存在）。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/geographypoint-from) [英文](https://learn.microsoft.com/en-us/powerquery-m/geographypoint-from) |
| Geometry.FromWellKnownText | 将以已知文本 (WKT) 格式表示几何值的文本转换为结构化记录。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/geometry-fromwellknowntext) [英文](https://learn.microsoft.com/en-us/powerquery-m/geometry-fromwellknowntext) |
| Geometry.ToWellKnownText | 将结构化几何点值转换为由开放地理空间信息联盟 (OGC) 定义的已知文本 (WKT) 表示形式，这种形式也是许多数据库（包括 SQL Server）使用的序列化格式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/geometry-towellknowntext) [英文](https://learn.microsoft.com/en-us/powerquery-m/geometry-towellknowntext) |
| GeometryPoint.From | 创建一个记录，该记录表示一个几何点的构成部分，例如 X 坐标、Y 坐标，以及 Z 坐标和度量值 (M)（如果存在）。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/geometrypoint-from) [英文](https://learn.microsoft.com/en-us/powerquery-m/geometrypoint-from) |
| Record.AddField | 给定字段 fieldName 的名称和值 value，将字段添加到记录 record。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/record-addfield) [英文](https://learn.microsoft.com/en-us/powerquery-m/record-addfield) |
| Record.Combine | 组合给定 records 中的记录。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/record-combine) [英文](https://learn.microsoft.com/en-us/powerquery-m/record-combine) |
| Record.Field | 返回 record 中指定 field 的值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/record-field) [英文](https://learn.microsoft.com/en-us/powerquery-m/record-field) |
| Record.FieldCount | 返回记录 record 中的字段数。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/record-fieldcount) [英文](https://learn.microsoft.com/en-us/powerquery-m/record-fieldcount) |
| Record.FieldNames | 将记录 record 中的字段名称作为文本返回。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/record-fieldnames) [英文](https://learn.microsoft.com/en-us/powerquery-m/record-fieldnames) |
| Record.FieldOrDefault | 返回记录 record 中指定字段 field 的值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/record-fieldordefault) [英文](https://learn.microsoft.com/en-us/powerquery-m/record-fieldordefault) |
| Record.FieldValues | 返回记录 record 中的字段值列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/record-fieldvalues) [英文](https://learn.microsoft.com/en-us/powerquery-m/record-fieldvalues) |
| Record.FromList | 根据给定的一个字段值 list 和一组字段返回一个记录。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/record-fromlist) [英文](https://learn.microsoft.com/en-us/powerquery-m/record-fromlist) |
| Record.FromTable | 返回记录表 table 中包含字段名称和值名称 {[Name = name, Value = value]} 的记录。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/record-fromtable) [英文](https://learn.microsoft.com/en-us/powerquery-m/record-fromtable) |
| Record.HasFields | 通过返回逻辑值（true 或 false），指示记录 record 是否具有 fields 中指定的字段。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/record-hasfields) [英文](https://learn.microsoft.com/en-us/powerquery-m/record-hasfields) |
| Record.RemoveFields | 返回一个记录，该记录从输入 record 中删除在列表 fields 中指定的所有字段。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/record-removefields) [英文](https://learn.microsoft.com/en-us/powerquery-m/record-removefields) |
| Record.RenameFields | 将 record 输入中的字段重命名为 renames 列表中指定的新字段名称后返回一条记录。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/record-renamefields) [英文](https://learn.microsoft.com/en-us/powerquery-m/record-renamefields) |
| Record.ReorderFields | 按照列表 fieldOrder 中指定的字段顺序对 record 中的字段重新排序后返回一条记录。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/record-reorderfields) [英文](https://learn.microsoft.com/en-us/powerquery-m/record-reorderfields) |
| Record.SelectFields | 从输入 record 返回一条记录，该记录仅包含在列表 fields 中指定的字段。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/record-selectfields) [英文](https://learn.microsoft.com/en-us/powerquery-m/record-selectfields) |
| Record.ToList | 返回包含输入 record 中的字段值的值列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/record-tolist) [英文](https://learn.microsoft.com/en-us/powerquery-m/record-tolist) |
| Record.ToTable | 返回一个表，其中包含 Name 和 Value 列，且 record 中的每个字段都占一行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/record-totable) [英文](https://learn.microsoft.com/en-us/powerquery-m/record-totable) |
| Record.TransformFields | 在将列表 transformOperations 中指定的转换应用到 record 后返回一条记录。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/record-transformfields) [英文](https://learn.microsoft.com/en-us/powerquery-m/record-transformfields) |
<h2 id='18'>18、替换器函数</h2>
<a href='#content'>返回目录</a>
| 函数名称 | 描述 | 链接 |
| :--: | :--: |:--: |
| Replacer.ReplaceText | 将原始 text 中的 old 文本替换为 new 文本。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/replacer-replacetext) [英文](https://learn.microsoft.com/en-us/powerquery-m/replacer-replacetext) |
| Replacer.ReplaceValue | 将原始 value 中的 old 值替换为 new 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/replacer-replacevalue) [英文](https://learn.microsoft.com/en-us/powerquery-m/replacer-replacevalue) |
<h2 id='19'>19、拆分器函数</h2>
<a href='#content'>返回目录</a>
| 函数名称 | 描述 | 链接 |
| :--: | :--: |:--: |
| Splitter.SplitByNothing | 返回不拆分且将其参数作为单元素列表返回的函数。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/splitter-splitbynothing) [英文](https://learn.microsoft.com/en-us/powerquery-m/splitter-splitbynothing) |
| Splitter.SplitTextByAnyDelimiter | 返回一个函数，它在任意指定的分隔符处将文本拆分为文本列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/splitter-splittextbyanydelimiter) [英文](https://learn.microsoft.com/en-us/powerquery-m/splitter-splittextbyanydelimiter) |
| Splitter.SplitTextByCharacterTransition | 返回一个函数，该函数根据从一种字符到另一种字符的转换过程将文本拆分为文本列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/splitter-splittextbycharactertransition) [英文](https://learn.microsoft.com/en-us/powerquery-m/splitter-splittextbycharactertransition) |
| Splitter.SplitTextByDelimiter | 返回一个函数，它根据指定的分隔符将文本拆分为文本列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/splitter-splittextbydelimiter) [英文](https://learn.microsoft.com/en-us/powerquery-m/splitter-splittextbydelimiter) |
| Splitter.SplitTextByEachDelimiter | 返回一个函数，它依次在每个指定的分隔符处将文本拆分为文本列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/splitter-splittextbyeachdelimiter) [英文](https://learn.microsoft.com/en-us/powerquery-m/splitter-splittextbyeachdelimiter) |
| Splitter.SplitTextByLengths | 返回一个函数，它按每个指定的长度将文本拆分为文本列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/splitter-splittextbylengths) [英文](https://learn.microsoft.com/en-us/powerquery-m/splitter-splittextbylengths) |
| Splitter.SplitTextByPositions | 返回一个函数，它在每个指定的位置将文本拆分为文本列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/splitter-splittextbypositions) [英文](https://learn.microsoft.com/en-us/powerquery-m/splitter-splittextbypositions) |
| Splitter.SplitTextByRanges | 返回一个函数，它根据指定的偏移量和长度将文本拆分为文本列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/splitter-splittextbyranges) [英文](https://learn.microsoft.com/en-us/powerquery-m/splitter-splittextbyranges) |
| Splitter.SplitTextByRepeatedLengths | 返回一个函数，此函数在指定的长度后反复将文本拆分为文本列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/splitter-splittextbyrepeatedlengths) [英文](https://learn.microsoft.com/en-us/powerquery-m/splitter-splittextbyrepeatedlengths) |
| Splitter.SplitTextByWhitespace | 返回一个函数，它在空白处将文本拆分为文本列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/splitter-splittextbywhitespace) [英文](https://learn.microsoft.com/en-us/powerquery-m/splitter-splittextbywhitespace) |
<h2 id='20'>20、表函数</h2>
<a href='#content'>返回目录</a>
| 函数名称 | 描述 | 链接 |
| :--: | :--: |:--: |
| ItemExpression.From | 返回 function 的主体的抽象语法树 (AST)，规范化为项表达式： 函数必须是包含 1 个参数的 lambda 函数。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/itemexpression-from) [英文](https://learn.microsoft.com/en-us/powerquery-m/itemexpression-from) |
| ItemExpression.Item | 表示项表达式中项的抽象语法树 (AST) 节点。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/itemexpression-item) [英文](https://learn.microsoft.com/en-us/powerquery-m/itemexpression-item) |
| RowExpression.Column | 返回一个抽象语法树 (AST)，该树表示对行表达式中行的列 columnName 的访问权限。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/rowexpression-column) [英文](https://learn.microsoft.com/en-us/powerquery-m/rowexpression-column) |
| RowExpression.From | 返回 function 主体的抽象语法树 (AST)，规范化为行表达式： 函数必须是包含 1 个参数的 lambda 函数。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/rowexpression-from) [英文](https://learn.microsoft.com/en-us/powerquery-m/rowexpression-from) |
| RowExpression.Row | 表示行表达式中行的抽象语法树 (AST) 节点。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/rowexpression-row) [英文](https://learn.microsoft.com/en-us/powerquery-m/rowexpression-row) |
| Table.AddColumn | 将名为 newColumnName 的列添加到表 table。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-addcolumn) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-addcolumn) |
| Table.AddFuzzyClusterColumn | 使用 columnName 的代表值将新列 newColumnName 添加到 table 中。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-addfuzzyclustercolumn) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-addfuzzyclustercolumn) |
| Table.AddIndexColumn | 使用显式位置值将名为 newColumnName 的列追加到 table 中。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-addindexcolumn) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-addindexcolumn) |
| Table.AddJoinColumn | 基于 key1（对于 table1）和 key2（对于 table2）所选择的键列的值的相等性，联接 table1 的行与 table2 的行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-addjoincolumn) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-addjoincolumn) |
| Table.AddKey | 向 table 添加一个键，其中 columns 是定义该键的列名称列表，isPrimary 指定该键是否为主键。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-addkey) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-addkey) |
| Table.AddRankColumn | 将名为 newColumnName 的列追加到 table，并使用由 comparisonCriteria 描述的一个或多个其他列进行排名。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-addrankcolumn) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-addrankcolumn) |
| Table.AggregateTableColumn | 将 table[column] 中的表聚合到包含这些表的聚合值的多个列中。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-aggregatetablecolumn) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-aggregatetablecolumn) |
| Table.AlternateRows | 保留初始偏移量，然后交替选取和跳过下列行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-alternaterows) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-alternaterows) |
| Table.ApproximateRowCount | 返回 table 中的近似行数，或者如果数据源不支持近似值，则返回错误。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-approximaterowcount) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-approximaterowcount) |
| Table.Buffer | 在内存中缓冲一个表，同时在计算期间使其与外部更改隔离。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-buffer) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-buffer) |
| Table.Column | 将表 table 中由 column 指定的数据列返回为列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-column) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-column) |
| Table.ColumnCount | 返回表 table 中的列数。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-columncount) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-columncount) |
| Table.ColumnNames | 以文本列表形式返回表 table 中的列名称。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-columnnames) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-columnnames) |
| Table.ColumnsOfType | 返回带有表 table 中与 listOfTypes 中指定的类型相匹配的列名的列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-columnsoftype) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-columnsoftype) |
| Table.Combine | 返回一个表，此表是合并表 tables 的列表的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-combine) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-combine) |
| Table.CombineColumns | 使用指定的组合程序函数将指定的列组合为一个新列。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-combinecolumns) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-combinecolumns) |
| Table.CombineColumnsToRecord | 将 table 的指定的列合并为名为 newColumnName 的新的记录值列，其中每个记录都具有与组合列的列名和值相对应的字段名称和值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-combinecolumnstorecord) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-combinecolumnstorecord) |
| Table.ConformToPageReader | 此函数仅计划供内部使用。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-conformtopagereader) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-conformtopagereader) |
| Table.Contains | 指示指定的记录 row 是否显示为 table 中的一行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-contains) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-contains) |
| Table.ContainsAll | 指示记录列表 rows 中的所有指定记录是否在 table 中显示为行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-containsall) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-containsall) |
| Table.ContainsAny | 指示记录 rows 列表中的任何指定记录是否在 table 中显示为行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-containsany) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-containsany) |
| Table.DemoteHeaders | 将列标题（即列名称）降级为值的第一行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-demoteheaders) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-demoteheaders) |
| Table.Distinct | 从表中删除重复的行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-distinct) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-distinct) |
| Table.DuplicateColumn | 将名为 columnName 的列复制到表 table。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-duplicatecolumn) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-duplicatecolumn) |
| Table.ExpandListColumn | 给定一个 table，其中 column 是一个值列表，将该列表拆分为每个值对应的一行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-expandlistcolumn) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-expandlistcolumn) |
| Table.ExpandRecordColumn | 给定输入 table 中的记录 column，创建一个表，其中包含对应记录中每个字段的列。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-expandrecordcolumn) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-expandrecordcolumn) |
| Table.ExpandTableColumn | 将 table[column] 中的表展开为多个行和列。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-expandtablecolumn) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-expandtablecolumn) |
| Table.FillDown | 从指定的 table 中返回一个表，其中前一个单元格的值会传播到指定的 columns 中下方值为 Null 的单元格。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-filldown) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-filldown) |
| Table.FillUp | 从指定的 table 中返回一个表，其中下一个单元的值传播到指定的 columns 上面值为 NULL 的单元。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-fillup) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-fillup) |
| Table.FilterWithDataTable | 此函数仅计划供内部使用。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-filterwithdatatable) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-filterwithdatatable) |
| Table.FindText | 返回表 table 中包含文本 text 的行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-findtext) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-findtext) |
| Table.First | 返回 table 的第一行，或如果表为空，则返回可选默认值 default。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-first) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-first) |
| Table.FirstN | 根据 countOrCondition 的值，返回 table 表的第一行： 如果 countOrCondition 是数字，则返回多个行（从顶部开始）。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-firstn) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-firstn) |
| Table.FirstValue | 返回表 table 的第一行的第一列或指定的默认值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-firstvalue) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-firstvalue) |
| Table.FromColumns | 从包含嵌套列表的列表 lists 中创建一个类型为 columns 的表，此表中具有列名称和值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-fromcolumns) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-fromcolumns) |
| Table.FromList | 通过将可选的拆分函数 splitter 应用于列表中的每一项，将列表 list 转换为表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-fromlist) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-fromlist) |
| Table.FromPartitions | 返回一个表，该表是组合一组分区表 partitions 的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-frompartitions) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-frompartitions) |
| Table.FromRecords | 将记录列表 records 转换为表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-fromrecords) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-fromrecords) |
| Table.FromRows | 从列表 rows 创建一个表，其中列表的每个元素都是包含单行列值的内部列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-fromrows) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-fromrows) |
| Table.FromValue | 创建一个表，该表中的列包含所提供的值或值列表 value。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-fromvalue) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-fromvalue) |
| Table.FuzzyGroup | 按每行的指定列 key 中模糊匹配的值对 table 的行进行分组。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-fuzzygroup) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-fuzzygroup) |
| Table.FuzzyJoin | 基于 key1（对于 table1）和 key2（对于 table2）所选择的键列的值的模糊匹配，联接 table1 的行与 table2 的行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-fuzzyjoin) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-fuzzyjoin) |
| Table.FuzzyNestedJoin | 基于 key1（对于 table1）和 key2（对于 table2）所选择的键列的值的模糊匹配，联接 table1 的行与 table2 的行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-fuzzynestedjoin) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-fuzzynestedjoin) |
| Table.Group | 按 key 定义的键列对 table 行进行分组。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-group) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-group) |
| Table.HasColumns | 指示 table 是否包含指定的列 columns。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-hascolumns) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-hascolumns) |
| Table.InsertRows | 返回一个表，此表包含插入到 table 中给定位置 offset 处的行 rows 的列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-insertrows) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-insertrows) |
| Table.IsDistinct | 指示 table 是否仅包含非重复行（没有重复项）。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-isdistinct) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-isdistinct) |
| Table.IsEmpty | 指示 table 是否包含任何行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-isempty) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-isempty) |
| Table.Join | 基于 key1（对于 table1）和 key2（对于 table2）所选择的键列的值的相等性，联接 table1 的行与 table2 的行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-join) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-join) |
| Table.Keys | 返回指定表的键。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-keys) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-keys) |
| Table.Last | 返回 table 的最后一行，或如果表为空，则返回可选默认值 default。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-last) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-last) |
| Table.LastN | 根据 countOrCondition 的值，返回 table 表的最后一行（或几行）： 如果 countOrCondition 是数字，则将返回从末尾 - countOrCondition 位置开始的多行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-lastn) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-lastn) |
| Table.MatchesAllRows | 指示 table 中的所有行是否与给定的 condition 匹配。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-matchesallrows) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-matchesallrows) |
| Table.MatchesAnyRows | 指示 table 中的任何行是否与给定的 condition 匹配。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-matchesanyrows) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-matchesanyrows) |
| Table.Max | 给定 comparisonCriteria，返回 table 中最大的行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-max) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-max) |
| Table.MaxN | 如果给定 comparisonCriteria，则返回 table 中最大的行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-maxn) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-maxn) |
| Table.Min | 如果给定 comparisonCriteria，则返回 table 中最小的行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-min) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-min) |
| Table.MinN | 如果给定 comparisonCriteria，则返回 table 中最小的行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-minn) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-minn) |
| Table.NestedJoin | 基于 key1（对于 table1）和 key2（对于 table2）所选择的键列的值的相等性，联接 table1 的行与 table2 的行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-nestedjoin) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-nestedjoin) |
| Table.Partition | 根据 column 和 hash 函数的值，将 table 分区为数量为 groups 的一系列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-partition) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-partition) |
| Table.PartitionValues | 返回有关如何对表进行分区的信息。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-partitionvalues) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-partitionvalues) |
| Table.Pivot | 在给定一对表示属性-值对的列的情况下，将属性列中的数据旋转为列标题。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-pivot) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-pivot) |
| Table.PositionOf | 返回 row 在指定 table 中第一个实例的位置。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-positionof) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-positionof) |
| Table.PositionOfAny | 返回 rows 列表第一个匹配项在 table 中的行位置。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-positionofany) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-positionofany) |
| Table.PrefixColumns | 返回一个表，其中来自所提供的 table 中的所有列名称均以给定的文本 prefix 为前缀，并加入一个句点，形成 prefix.ColumnName 格式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-prefixcolumns) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-prefixcolumns) |
| Table.Profile | 返回 table 中列的配置文件。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-profile) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-profile) |
| Table.PromoteHeaders | 将第一行值升级为新的列标题（即列名）。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-promoteheaders) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-promoteheaders) |
| Table.Range | 从以指定 offset 开始的 table 返回行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-range) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-range) |
| Table.RemoveColumns | 从提供的 table 删除指定的 columns。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-removecolumns) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-removecolumns) |
| Table.RemoveFirstN | 返回一个表，该表不包含表 table 中前数行 countOrCondition（行数为指定数字）。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-removefirstn) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-removefirstn) |
| Table.RemoveLastN | 返回一个表，该表不包含表 table 中最后的 countOrCondition 行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-removelastn) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-removelastn) |
| Table.RemoveMatchingRows | 从 table 中删除所有出现的指定 rows。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-removematchingrows) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-removematchingrows) |
| Table.RemoveRows | 从指定的 offset 开始，从 table 的开头删除 count 行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-removerows) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-removerows) |
| Table.RemoveRowsWithErrors | 返回一个表，其中删除了在至少一个单元格中包含错误的输入表中的行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-removerowswitherrors) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-removerowswitherrors) |
| Table.RenameColumns | 对表 table 中的列执行给定的重命名。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-renamecolumns) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-renamecolumns) |
| Table.ReorderColumns | 返回输入 table 中的表，其中，列是按 columnOrder 指定的顺序排列的。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-reordercolumns) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-reordercolumns) |
| Table.Repeat | 返回一个表，表中的行来自输入 table 且重复了指定的 count 次。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-repeat) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-repeat) |
| Table.ReplaceErrorValues | 将 table 的指定列中的错误值替换为 errorReplacement 列表中的新值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-replaceerrorvalues) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-replaceerrorvalues) |
| Table.ReplaceKeys | 替换指定表的键。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-replacekeys) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-replacekeys) |
| Table.ReplaceMatchingRows | 使用提供的行替换 table 中的所有指定行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-replacematchingrows) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-replacematchingrows) |
| Table.ReplaceRelationshipIdentity | 此函数仅计划供内部使用。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-replacerelationshipidentity) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-replacerelationshipidentity) |
| Table.ReplaceRows | 在输入 table 中，用指定的 rows 替换指定数目的行 count，并在 offset 后开始。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-replacerows) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-replacerows) |
| Table.ReplaceValue | 在 table 的指定列中将 oldValue 替换为 newValue。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-replacevalue) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-replacevalue) |
| Table.ReverseRows | 从输入 table 返回一个表，其中的行按相反的顺序排列。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-reverserows) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-reverserows) |
| Table.RowCount | 返回 table 中的行数。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-rowcount) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-rowcount) |
| Table.Schema | 返回描述 table 列的表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-schema) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-schema) |
| Table.SelectColumns | 返回仅具有指定的 columns 的 table。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-selectcolumns) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-selectcolumns) |
| Table.SelectRows | 从 table 返回与选择 condition 匹配的行的表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-selectrows) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-selectrows) |
| Table.SelectRowsWithErrors | 返回一个表，其中仅包含输入表中至少一个单元格中包含错误的那些行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-selectrowswitherrors) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-selectrowswitherrors) |
| Table.SingleRow | 返回包含一行 table 中的单行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-singlerow) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-singlerow) |
| Table.Skip | 返回一个表，该表不包含表 table 中前数行 countOrCondition（行数为指定数字）。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-skip) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-skip) |
| Table.Sort | 使用一个或多个列名的列表和可选的 comparisonCriteria（格式为 { { col1, comparisonCriteria }, {col2} }）对 table 排序。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-sort) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-sort) |
| Table.Split | 将 table 拆分为表列表，其中列表的第一个元素是包含源表中前 pageSize 行的表，列表的下一个元素是包含源表中接下来 pageSize 行的表，以此类推。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-split) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-split) |
| Table.SplitAt | 返回一个列表，其中包含两个表：一个表包含 table 的前 N 行（由 count 指定），一个表包含 table 的其余行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-splitat) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-splitat) |
| Table.SplitColumn | 使用指定的拆分器函数将指定的列拆分为一组其他列。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-splitcolumn) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-splitcolumn) |
| Table.StopFolding | 防止任何下游操作针对 table 中的原始数据源运行。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-stopfolding) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-stopfolding) |
| Table.ToColumns | 从表 table 中创建嵌套列表的列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-tocolumns) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-tocolumns) |
| Table.ToList | 通过将指定的组合函数应用于表中的每一行值，将表转换为列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-tolist) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-tolist) |
| Table.ToRecords | 将表 table 转换为记录列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-torecords) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-torecords) |
| Table.ToRows | 从表 table 中创建嵌套列表的列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-torows) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-torows) |
| Table.TransformColumnNames | 使用给定的 nameGenerator 函数转换列名。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-transformcolumnnames) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-transformcolumnnames) |
| Table.TransformColumns | 通过应用 transformOperations 中列出的每个列操作来转换 table（格式为 { column name, transformation } 或 { column name, transformation, new column type }）。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-transformcolumns) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-transformcolumns) |
| Table.TransformColumnTypes | 通过对在参数 typeTransformations 中指定的列应用转换操作（其中格式为 { column name, type name}），使用可选参数 culture 中的指定区域性（例如“en-US”），从输入 table 中返回一个表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-transformcolumntypes) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-transformcolumntypes) |
| Table.TransformRows | 通过将 transform 操作应用于 table 中的每一行来创建 list。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-transformrows) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-transformrows) |
| Table.Transpose | 使列成为行，并使行成为列。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-transpose) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-transpose) |
| Table.Unpivot | 将表中的一组列转换为属性-值对，并与每行中的剩余值相结合。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-unpivot) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-unpivot) |
| Table.UnpivotOtherColumns | 将指定集以外的所有列转换为属性值对，与每行中的剩余值相合并。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-unpivotothercolumns) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-unpivotothercolumns) |
| Table.View | 返回 table 的视图，向视图应用运算时，会使用 handlers 中指定的函数代替运算的默认行为。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-view) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-view) |
| Table.ViewError | 根据 errorRecord 创建修改后的错误记录，该记录在视图上定义的处理程序引发时（通过 Table.View）将不会触发回退。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-viewerror) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-viewerror) |
| Table.ViewFunction | 基于 function 创建视图函数，此函数可以在 Table.View 创建的视图中处理。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/table-viewfunction) [英文](https://learn.microsoft.com/en-us/powerquery-m/table-viewfunction) |
| Tables.GetRelationships | 获取一组表之间的关系。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/tables-getrelationships) [英文](https://learn.microsoft.com/en-us/powerquery-m/tables-getrelationships) |
| #table | 从 columns 和 rows 创建表值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/sharptable) [英文](https://learn.microsoft.com/en-us/powerquery-m/sharptable) |
<h2 id='21'>21、时间函数</h2>
<a href='#content'>返回目录</a>
| 函数名称 | 描述 | 链接 |
| :--: | :--: |:--: |
| Time.EndOfHour | 返回由 dateTime 表示的小时结束值，包括分数秒。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/time-endofhour) [英文](https://learn.microsoft.com/en-us/powerquery-m/time-endofhour) |
| Time.From | 从给定的 value 返回 time 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/time-from) [英文](https://learn.microsoft.com/en-us/powerquery-m/time-from) |
| Time.FromText | 从文本表示形式 text 创建一个 time 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/time-fromtext) [英文](https://learn.microsoft.com/en-us/powerquery-m/time-fromtext) |
| Time.Hour | 返回所提供的 time、datetime 或datetimezone 值、dateTime 的小时部分。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/time-hour) [英文](https://learn.microsoft.com/en-us/powerquery-m/time-hour) |
| Time.Minute | 返回所提供的 time、datetime 或 datetimezone 值的分钟部分，dateTime。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/time-minute) [英文](https://learn.microsoft.com/en-us/powerquery-m/time-minute) |
| Time.Second | 返回所提供的 time、datetime 或 datetimezone 值 dateTime 的秒部分。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/time-second) [英文](https://learn.microsoft.com/en-us/powerquery-m/time-second) |
| Time.StartOfHour | 返回由 dateTime 表示的小时开始值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/time-startofhour) [英文](https://learn.microsoft.com/en-us/powerquery-m/time-startofhour) |
| Time.ToRecord | 返回包含给定时间值 time 的各个部分的记录。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/time-torecord) [英文](https://learn.microsoft.com/en-us/powerquery-m/time-torecord) |
| Time.ToText | 返回 time 的文本化表示形式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/time-totext) [英文](https://learn.microsoft.com/en-us/powerquery-m/time-totext) |
| #time | 从表示小时、分钟和（小数）秒的数值创建 time 值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/sharptime) [英文](https://learn.microsoft.com/en-us/powerquery-m/sharptime) |
<h2 id='22'>22、类型函数</h2>
<a href='#content'>返回目录</a>
| 函数名称 | 描述 | 链接 |
| :--: | :--: |:--: |
| Type.AddTableKey | 向给定表类型添加键。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/type-addtablekey) [英文](https://learn.microsoft.com/en-us/powerquery-m/type-addtablekey) |
| Type.ClosedRecord | 返回给定 recordtype 的已关闭版本（或者如果已关闭，则为同一类型）。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/type-closedrecord) [英文](https://learn.microsoft.com/en-us/powerquery-m/type-closedrecord) |
| Type.Facets | 返回一条包含 type 的 Facet 的记录。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/type-facets) [英文](https://learn.microsoft.com/en-us/powerquery-m/type-facets) |
| Type.ForFunction | 从 signature 创建 function type（ReturnType 和 Parameters 的记录），再创建 min（调用函数所需的最少参数数目）。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/type-forfunction) [英文](https://learn.microsoft.com/en-us/powerquery-m/type-forfunction) |
| Type.ForRecord | 返回一个类型，此类型表示对字段具有特定类型约束的记录。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/type-forrecord) [英文](https://learn.microsoft.com/en-us/powerquery-m/type-forrecord) |
| Type.FunctionParameters | 返回一个记录，它的字段值设置为 type 的参数名称，值设置为相应的类型。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/type-functionparameters) [英文](https://learn.microsoft.com/en-us/powerquery-m/type-functionparameters) |
| Type.FunctionRequiredParameters | 返回一个数字，表明调用函数的输入 type 所需参数的最小数量。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/type-functionrequiredparameters) [英文](https://learn.microsoft.com/en-us/powerquery-m/type-functionrequiredparameters) |
| Type.FunctionReturn | 返回由函数 type 返回的类型。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/type-functionreturn) [英文](https://learn.microsoft.com/en-us/powerquery-m/type-functionreturn) |
| Type.Is | 确定 type1 的值是否始终与 type2 兼容。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/type-is) [英文](https://learn.microsoft.com/en-us/powerquery-m/type-is) |
| Type.IsNullable | 如果类型是 nullable 类型，则返回 true；否则返回 false。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/type-isnullable) [英文](https://learn.microsoft.com/en-us/powerquery-m/type-isnullable) |
| Type.IsOpenRecord | 返回一个 logical，此值指示记录 type 是否处于打开状态。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/type-isopenrecord) [英文](https://learn.microsoft.com/en-us/powerquery-m/type-isopenrecord) |
| Type.ListItem | 从列表 type 中返回项类型。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/type-listitem) [英文](https://learn.microsoft.com/en-us/powerquery-m/type-listitem) |
| Type.NonNullable | 从 type 返回非 nullable 类型。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/type-nonnullable) [英文](https://learn.microsoft.com/en-us/powerquery-m/type-nonnullable) |
| Type.OpenRecord | 返回给定 recordtype（或同一类型，如果其已打开）的打开版本。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/type-openrecord) [英文](https://learn.microsoft.com/en-us/powerquery-m/type-openrecord) |
| Type.RecordFields | 返回描述 type 记录字段的记录。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/type-recordfields) [英文](https://learn.microsoft.com/en-us/powerquery-m/type-recordfields) |
| Type.ReplaceFacets | 将 type 的 facet 替换为记录 facets 中包含的 facet。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/type-replacefacets) [英文](https://learn.microsoft.com/en-us/powerquery-m/type-replacefacets) |
| Type.ReplaceTableKeys | 返回一个新的表类型，其中所有键都替换为指定的键列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/type-replacetablekeys) [英文](https://learn.microsoft.com/en-us/powerquery-m/type-replacetablekeys) |
| Type.TableColumn | 返回表类型 tableType 中列 column 的类型。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/type-tablecolumn) [英文](https://learn.microsoft.com/en-us/powerquery-m/type-tablecolumn) |
| Type.TableKeys | 返回给定表类型的可能为空的键列表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/type-tablekeys) [英文](https://learn.microsoft.com/en-us/powerquery-m/type-tablekeys) |
| Type.TableRow | 返回指定表类型的行类型。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/type-tablerow) [英文](https://learn.microsoft.com/en-us/powerquery-m/type-tablerow) |
| Type.TableSchema | 返回描述 tableType 列的表。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/type-tableschema) [英文](https://learn.microsoft.com/en-us/powerquery-m/type-tableschema) |
| Type.Union | 返回 types 中类型的联合。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/type-union) [英文](https://learn.microsoft.com/en-us/powerquery-m/type-union) |
<h2 id='23'>23、Uri 函数</h2>
<a href='#content'>返回目录</a>
| 函数名称 | 描述 | 链接 |
| :--: | :--: |:--: |
| Uri.BuildQueryString | 将记录 query 汇编入 URI 查询字符串，根据需要转义字符。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/uri-buildquerystring) [英文](https://learn.microsoft.com/en-us/powerquery-m/uri-buildquerystring) |
| Uri.Combine | 返回一个绝对 URI，这是输入 baseUri 和 relativeUri 的组合。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/uri-combine) [英文](https://learn.microsoft.com/en-us/powerquery-m/uri-combine) |
| Uri.EscapeDataString | 根据 RFC 3986 的规则对输入 data 中的特殊字符进行编码。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/uri-escapedatastring) [英文](https://learn.microsoft.com/en-us/powerquery-m/uri-escapedatastring) |
| Uri.Parts | 以记录形式返回输入 absoluteUri 的组成部分，包含方案、主机、端口、路径、查询、片段、用户名和密码等值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/uri-parts) [英文](https://learn.microsoft.com/en-us/powerquery-m/uri-parts) |
<h2 id='24'>24、值函数</h2>
<a href='#content'>返回目录</a>
| 函数名称 | 描述 | 链接 |
| :--: | :--: |:--: |
| DirectQueryCapabilities.From | 此函数仅计划供内部使用。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/directquerycapabilities-from) [英文](https://learn.microsoft.com/en-us/powerquery-m/directquerycapabilities-from) |
| Embedded.Value | 在嵌入的混合 Web 应用程序中按名称访问值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/embedded-value) [英文](https://learn.microsoft.com/en-us/powerquery-m/embedded-value) |
| Excel.ShapeTable | 此函数仅计划供内部使用。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/excel-shapetable) [英文](https://learn.microsoft.com/en-us/powerquery-m/excel-shapetable) |
| Graph.Nodes | 此函数仅计划供内部使用。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/graph-nodes) [英文](https://learn.microsoft.com/en-us/powerquery-m/graph-nodes) |
| Progress.DataSourceProgress | 此函数仅计划供内部使用。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/progress-datasourceprogress) [英文](https://learn.microsoft.com/en-us/powerquery-m/progress-datasourceprogress) |
| SqlExpression.SchemaFrom | 此函数仅计划供内部使用。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/sqlexpression-schemafrom) [英文](https://learn.microsoft.com/en-us/powerquery-m/sqlexpression-schemafrom) |
| SqlExpression.ToExpression | 使用 environment 定义的可用标识符将提供的 sql 查询转换为 M 代码。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/sqlexpression-toexpression) [英文](https://learn.microsoft.com/en-us/powerquery-m/sqlexpression-toexpression) |
| Value.Add | 返回 value1 和 value2 的总和。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/value-add) [英文](https://learn.microsoft.com/en-us/powerquery-m/value-add) |
| Value.Alternates | 表示通过 Value.Expression(Value.Optimize(...)) 获取的查询计划表达式中的替代查询计划。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/value-alternates) [英文](https://learn.microsoft.com/en-us/powerquery-m/value-alternates) |
| Value.As | 如果值与指定类型兼容，则返回该值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/value-as) [英文](https://learn.microsoft.com/en-us/powerquery-m/value-as) |
| Value.Compare | 根据第一个值是小于、等于还是大于第二个值，返回 -1、0 或 1。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/value-compare) [英文](https://learn.microsoft.com/en-us/powerquery-m/value-compare) |
| Value.Divide | 返回 value2 除以 value1 的结果。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/value-divide) [英文](https://learn.microsoft.com/en-us/powerquery-m/value-divide) |
| Value.Equals | 如果值 value1 等于值 value2，则返回 true；否则返回 false。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/value-equals) [英文](https://learn.microsoft.com/en-us/powerquery-m/value-equals) |
| Value.Expression | 返回表示值表达式的抽象语法树 (AST)。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/value-expression) [英文](https://learn.microsoft.com/en-us/powerquery-m/value-expression) |
| Value.Firewall | 此函数仅计划供内部使用。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/value-firewall) [英文](https://learn.microsoft.com/en-us/powerquery-m/value-firewall) |
| Value.FromText | 从文本表示形式 text 解码一个值，并将其解释为具有适当类型的值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/value-fromtext) [英文](https://learn.microsoft.com/en-us/powerquery-m/value-fromtext) |
| Value.Is | 确定值是否与指定类型兼容。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/value-is) [英文](https://learn.microsoft.com/en-us/powerquery-m/value-is) |
| Value.Lineage | 此函数仅计划供内部使用。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/value-lineage) [英文](https://learn.microsoft.com/en-us/powerquery-m/value-lineage) |
| Value.Metadata | 返回包含输入的元数据的记录。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/value-metadata) [英文](https://learn.microsoft.com/en-us/powerquery-m/value-metadata) |
| Value.Multiply | 返回 value1 和 value2 的乘积。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/value-multiply) [英文](https://learn.microsoft.com/en-us/powerquery-m/value-multiply) |
| Value.NativeQuery | 使用 parameters 中指定的参数和 options 中指定的选项，根据 target 计算 query。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/value-nativequery) [英文](https://learn.microsoft.com/en-us/powerquery-m/value-nativequery) |
| Value.NullableEquals | 如果任一参数 value1 或 value2 为 Null，则返回 Null，否则等同于 Value.Equals。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/value-nullableequals) [英文](https://learn.microsoft.com/en-us/powerquery-m/value-nullableequals) |
| Value.Optimize | 在 Value.Expression 中使用时，如果 value 表示可优化的查询，则此函数指示应返回已优化的表达式。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/value-optimize) [英文](https://learn.microsoft.com/en-us/powerquery-m/value-optimize) |
| Value.RemoveMetadata | 去除元数据的输入。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/value-removemetadata) [英文](https://learn.microsoft.com/en-us/powerquery-m/value-removemetadata) |
| Value.ReplaceMetadata | 替换输入的元数据信息。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/value-replacemetadata) [英文](https://learn.microsoft.com/en-us/powerquery-m/value-replacemetadata) |
| Value.ReplaceType | 将 value 的类型替换为提供的 type。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/value-replacetype) [英文](https://learn.microsoft.com/en-us/powerquery-m/value-replacetype) |
| Value.Subtract | 返回 value1 和 value2 的差值。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/value-subtract) [英文](https://learn.microsoft.com/en-us/powerquery-m/value-subtract) |
| Value.Traits | 此函数仅计划供内部使用。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/value-traits) [英文](https://learn.microsoft.com/en-us/powerquery-m/value-traits) |
| Value.Type | 返回给定值的类型。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/value-type) [英文](https://learn.microsoft.com/en-us/powerquery-m/value-type) |
| Value.VersionIdentity | 返回 value 的版本标识，如果没有版本，则返回 null。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/value-versionidentity) [英文](https://learn.microsoft.com/en-us/powerquery-m/value-versionidentity) |
| Value.Versions | 返回一个导航表，其中包含 value 的可用版本。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/value-versions) [英文](https://learn.microsoft.com/en-us/powerquery-m/value-versions) |
| Value.ViewError | 此函数仅计划供内部使用。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/value-viewerror) [英文](https://learn.microsoft.com/en-us/powerquery-m/value-viewerror) |
| Value.ViewFunction | 此函数仅计划供内部使用。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/value-viewfunction) [英文](https://learn.microsoft.com/en-us/powerquery-m/value-viewfunction) |
| Variable.Value | 此函数仅计划供内部使用。 | [中文](https://learn.microsoft.com/zh-cn/powerquery-m/variable-value) [英文](https://learn.microsoft.com/en-us/powerquery-m/variable-value) |