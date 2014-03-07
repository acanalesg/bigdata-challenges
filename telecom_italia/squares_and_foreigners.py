from dumbo import sumreducer

def float_zero(str):
    try:
        return float(str)
    except:
        return 0.0


def parse_mapper(key, value):
    value = value.strip() + "\t".join(["0"]*6)
    squareid, dt, country, smsin, smsout, callin, callout = value.split('	')[0:7]
    country = country.strip()
    if country not in ['39', '0']:
        yield (squareid, country), sum(float_zero(s) for s in [smsin, smsout, callin, callout])


def mid_mapper(key, value):
    # squareid, (weight, countrycode)
    yield key[0], (value, key[1])


def topn_reducer(key, values):
    values = sorted(list(values), reverse=True)

    yield ",".join(str(s) for s in ('top', key) + values[0] + ('',)), ""
    for v in values:
        yield ",".join(str(s) for s in ('all', key) + v +('',)), ""


def runner(job):
    opts = [("inputformat", "text"), ("outputformat", "sequencefile"), ]
    o1 = job.additer(parse_mapper, sumreducer, opts=opts)

    opts = [("inputformat", "sequencefile"), ("outputformat", "text"), ]
    o2 = job.additer(mid_mapper, topn_reducer, opts=opts)


if __name__ == "__main__":
    from dumbo import main
    main(runner)
