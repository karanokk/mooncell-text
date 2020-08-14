"""See https://fgo.wiki/api.php?action=help&modules=query"""


class QueryParameter:
    # 要为已查询页面获取的属性。
    prop = 'prop'

    # 要工作的标题列表。通过|或替代物隔开各值。 值的最大数量是50
    titles = 'titles'

    # 要工作的页面ID列表。通过|或替代物隔开各值。 值的最大数量是50
    pageids = 'pageids'

    # 要工作的修订ID列表。通过|或替代物隔开各值。 值的最大数量是50
    revids = 'revids'

    # 通过执行指定查询模块获得页面列表以工作。
    generator = 'generator'


class QueryProp:
    # 页面属于的所有分类列表。
    categories = 'categories'

    # 返回有关给定分类的信息。
    categoryinfo = 'categoryinfo'

    # 获取对一个页面的登录贡献者列表和匿名贡献数。
    contributors = 'contributors'

    # 获取删除的修订版本信息。
    deletedrevisions = 'deletedrevisions'

    # 根据哈希值列出此给定文件的所有副本。
    duplicatefiles = 'duplicatefiles'

    # 从指定页面返回所有外部URL（非跨wiki链接）。
    extlinks = 'extlinks'

    # 查找所有使用指定文件的页面。
    fileusage = 'fileusage'

    # 返回文件信息和上传历史。
    imageinfo = 'imageinfo'

    # 返回指定页面上包含的所有文件。
    images = 'images'

    # 获取基本页面信息。
    info = 'info'

    # 从指定页面返回所有跨wiki链接。
    iwlinks = 'iwlinks'

    # 从指定页面返回所有跨语言链接。
    langlinks = 'langlinks'

    # 从指定页面返回所有链接。
    links = 'links'

    # 查找所有链接至指定页面的页面。
    linkshere = 'linkshere'

    # 获取页面内容中定义的各种页面属性。
    pageprops = 'pageprops'

    # 返回至指定页面的所有重定向。
    redirects = 'redirects'

    # 返回与指定页面相关联的参考文献的数据表示法。
    references = 'references'

    # 获取修订版本信息。
    revisions = 'revisions'

    # 返回用于藏匿文件的文件信息。
    stashimageinfo = 'stashimageinfo'

    # 返回指定页面上所有被嵌入的页面。
    templates = 'templates'

    # 查找所有嵌入指定页面的页面。
    transcludedin = ''
