import options

def test_optdict():
    d = options.OptDict()
    d['x'] = 5
    d['y'] = 4
    d['z'] = 99
    d['no_other_thing'] = 5
    assert d.x == 5
    assert d['x'] == 5
    assert d.y == 4
    assert d.z == 99
    assert d.no_z == False
    assert d.no_other_thing == True
    assert d.other_thing == False
    try:
        d.p
    except KeyError:
        pass
    else:
        assert False
    print d
    print repr(d)

def test_optdict_more():
    d = options.OptDict()
    d['x'] = 5
    d['y'] = 4
    d['z'] = 99
    d['no_foo'] = 7
    d['no-bar'] = 11

    for k, v in [('x', 5), ('y', 4), ('z', 99)]:
        assert getattr(d, k) == v
        assert d[k] == v
        assert getattr(d, "no_%s"%k) == False
        assert d["no_%s"%k] == False
        assert d["no-%s"%k] == False

    for k in ['foo', 'bar']:
        assert d[k] == False
        assert getattr(d, k) == False
        assert d["no_%s"%k] == True
        assert d["no-%s"%k] == True

optspec = """
prog <optionset> [stuff...]
prog [-t] <boggle>
--
t       test
q,quiet   quiet
l,longoption=   long option with parameters and a really really long description that will require wrapping
p= short option with parameters
onlylong  long option with no short
neveropt never called options
deftest1=  a default option with default [1]
deftest2=  a default option with [1] default [2]
deftest3=  a default option with [3] no actual default
deftest4=  a default option with [[square]]
deftest5=  a default option with "correct" [[square]
no-stupid  disable stupidity
#,compress=  set compression level [5]
"""


def test_options():
    o = options.Options(optspec)
    (opt, flags, extra) = o.parse(['-tttqp', 7, '--longoption', '19',
                                 'hanky', '--onlylong', '-7'])
    assert flags[0] == ('-t', '')
    assert flags[1] == ('-t', '')
    assert flags[2] == ('-t', '')
    assert flags[3] == ('-q', '')
    assert flags[4] == ('-p', 7)
    assert flags[5] == ('--longoption', '19')
    assert extra == ['hanky']
    assert opt.t == 3
    assert opt.q == 1
    assert opt.p == 7
    assert opt.l == 19
    assert opt.onlylong == 1
    assert opt.neveropt == None
    assert opt.deftest1 == 1
    assert opt.deftest2 == 2
    assert opt.deftest3 == None
    assert opt.deftest4 == None
    assert opt.deftest5 == '[square'
    assert (opt.stupid, opt.no_stupid) == (True, False)
    assert opt['#'] == 7
    assert opt.compress == 7

    (opt, flags, extra) = o.parse(['--onlylong', '-t', '--no-onlylong'])
    assert opt.t == 1
    assert opt.q ==  None
    assert opt.onlylong == 0


def test_usagestr():
    o = options.Options(optspec)
    expected = """
usage: prog <optionset> [stuff...]
   or: prog [-t] <boggle>

    -t                    test
    -q, --quiet           quiet
    -l, --longoption ...  long option with parameters and a really really long description that will require wrapping
    -p ...                short option with parameters
    --onlylong            long option with no short
    --neveropt            never called options
    --deftest1 ...        a default option with default [1]
    --deftest2 ...        a default option with [1] default [2]
    --deftest3 ...        a default option with [3] no actual default
    --deftest4 ...        a default option with [[square]]
    --deftest5 ...        a default option with "correct" [[square]
    --no-stupid           disable stupidity
    -#, --compress ...    set compression level [5]""".strip()
    assert o._usagestr.strip() == expected


def test_parse():
    o = options.Options(optspec, onabort=None)
    assert o.parse(['-h']) == None

    (opt, flags, extra) = o.parse(["-t"])

    assert flags == [('-t', '')]
    assert not extra


def test_intify():
    assert options._intify(1) is 1
    assert options._intify("1") is 1
    assert options._intify("one") is "one"
    assert options._intify(None) is None
    assert options._intify(True) is True


def test_atoi():
    assert options._atoi(1) is 1
    assert options._atoi("one") is 0
    assert options._atoi("1") is 1
    assert options._atoi(None) is 0
    assert options._atoi(True) is 1


def test_remove_negative_kv():
    assert options._remove_negative_kv("no_foo", 0) == ("foo", True)
    assert options._remove_negative_kv("no-foo", "one") == ("foo", False)


def test_remove_negative_k():
    assert options._remove_negative_k("no_foo") == ("foo")
    assert options._remove_negative_k("no-foo") == ("foo")
