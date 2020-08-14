"""See https://fgo.wiki/api.php?action=help&modules=parse"""


class ParseParameter:
    # 文本属于的页面标题。如果省略，contentmodel就必须被指定，且API将作为标题使用。
    title = 'title'

    # 要解析的文本。使用title或contentmodel以控制内容模型。
    text = 'text'

    # 修订版本ID，用于{{REVISIONID}}和类似变体。
    revid = 'revid'

    # 要解析的摘要。
    summary = 'summary'

    # 解析此页的内容。不能与text和title一起使用。
    page = 'page'

    # 解析此页的内容。覆盖page。
    pageid = 'pageid'

    # 解析该修订版本的内容。覆盖page和pageid。
    oldid = 'oldid'

    # 要获取的信息束
    prop = 'prop'
    
    # 要用于包裹解析输出的CSS类。
    wrapoutputclass = 'wrapoutputclass'


class ParseProp:
    # 提供wiki文本中的被解析文本。
    text = 'text'

    # 在被解析的wiki文本中提供语言链接。
    langlinks = 'langlinks'

    # 在被解析的wiki文本中提供分类。
    categories = 'categories'

    # 提供HTML版本分类。
    categorieshtml = 'categorieshtml'

    # 在被解析的wiki文本中提供内部链接。
    links = 'links'

    # 在被解析的wiki文本中提供模板。
    templates = 'templates'

    # 在被解析的wiki文本中提供图片。
    images = 'images'

    # 在被解析的wiki文本中提供外部链接。
    externallinks = 'externallinks'

    # 在被解析的wiki文本中提供段落。
    sections = 'sections'

    # 添加被解析页面的修订ID。
    revid = 'revid'

    # 为被解析的wiki文本添加标题。
    displaytitle = 'displaytitle'

    # 提供页面的被解析<head>。
    headhtml = 'headhtml'

    # 提供在页面中使用的ResourceLoader模块。要加载，请使用mw.loader.using''。无论jsconfigvars还是encodedjsconfigvars都必须与modules共同被请求。 = ''
    modules = 'modules'

    # 针对页面提供JavaScript配置变量。要应用，请使用mw.config.set''。
    jsconfigvars = 'jsconfigvars'

    # 针对页面提供JavaScript配置变量为一个JSON字符串。
    encodedjsconfigvars = 'encodedjsconfigvars'

    # 提供页面上使用的页面状态指示器的HTML。
    indicators = 'indicators'

    # 在被解析的wiki文本中提供跨wiki链接。
    iwlinks = 'iwlinks'

    # 提供被解析的原始wiki文本。
    wikitext = 'wikitext'

    # 提供多种定义在被解析的wiki文本中的属性。
    properties = 'properties'

    # 以结构化的方式提供限制报告。如果disablelimitreport被设定则不提供数据。
    limitreportdata = 'limitreportdata'

    # 提供限制报告的HTML版本。当disablelimitreport被设置时不会提供数据。
    limitreporthtml = 'limitreporthtml'

    # 修订内容的XML解析树（需要内容模型wikitext）
    parsetree = 'parsetree'

    # 在解析内容时提供发生的警告
    parsewarnings = 'parsewarnings'
