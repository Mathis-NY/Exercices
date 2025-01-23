from twttr import shorten

def main ():
    test_twttr()



def test_twttr():
    assert shorten("mathiscoll") == "mthscll"
    assert shorten("MATHISCOLL") == "MTHSCLL"
    assert shorten("2018") == "2018"
    assert shorten("/§;:!ù$") == "/§;:!ù$"
    assert shorten("MatHisCoLL") == "MtHsCLL"


if __name__ == "__main__":
    main()
