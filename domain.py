"""
Author: Ty Klabacka
Date: Feb 4, 2022


Functionality: Program extracts and returns the domain name from the url.
"""

def domain_name(url):
    """Returns domain from messy URL"""
    lyst = ['http:','https:', 'www']
    replaced = url.replace('.', ' ').replace('/', ' ').split() 
    for element in lyst:
        if element in replaced:
            replaced.remove(element)
    return replaced[0]

def main():
    assert(domain_name("http://google.com") == "google")
    assert(domain_name("http://google.co.jp") == "google")
    assert(domain_name("www.xakep.ru") == "xakep")
    assert(domain_name("https://youtube.com") == "youtube")
    assert(domain_name("https://python-reference.readthedocs.io/en/latest/docs/list/") == "python-reference")
    
if __name__ == "__main__":
    main()
