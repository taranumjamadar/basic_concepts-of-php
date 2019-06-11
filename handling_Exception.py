def safe_run(f,x):
    try:
        f(x)
    except ValueError:
       return 'ValueError'
    except ValueError:
       return 'TypeError'
    else:
       return 'OK'