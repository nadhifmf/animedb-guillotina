from guillotina import configure


app_settings = {
    # provide custom application settings here...
}

def includeme(root):
    """
    custom application initialization here
    """
    configure.scan('animedb.service.template')
    configure.scan('animedb.service.alldata')
    configure.scan('animedb.service.pull_mal')
    configure.scan('animedb.service.search_mal')
    configure.scan('animedb.content.folder_s')
    configure.scan('animedb.api')
    configure.scan('animedb.install')
    
    
