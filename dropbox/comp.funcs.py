def checkio(f,g):
    def h(*args,**kwargs):
        try:
            fret = f(*args, **kwargs)
        except Exception as e:
            fret = None

        try:
            gret = g(*args, **kwargs)
        except Exception as e:
            gret = None

        if fret is None and gret is None:
            return (None, "both_error")
        elif fret is None:
            return (gret, "f_error")
        elif gret is None:
            return (fret, "g_error")
        elif fret != gret:
            return (fret, "different")
        else:
            return (fret, "same")

    return h
