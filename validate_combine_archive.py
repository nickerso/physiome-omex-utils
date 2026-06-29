import sys
import libcombine

def print_omex_contents(archive):
    print("Archive has {} entries".format(archive.getNumEntries()))
    for i in range(archive.getNumEntries()):
        entry = archive.getEntry(i)
        print(" {0}: location: {1} format: {2}".format(i, entry.getLocation(), entry.getFormat()))
        for j in range(entry.getNumCrossRefs()):
            print("  {0}: crossRef location {1}".format(j, entry.getCrossRef(j).getLocation()))

def validate_omex_file(filename):
    archive = libcombine.CombineArchive()
    if archive.initializeFromArchive(filename) is False:
        print("Invalid COMBINE Archive: {}".format(filename))
        return None

    print('*' * 50)
    print('Valid archive:', filename)
    print('*' * 50)
    print_omex_contents(archive)


def print_usage():
    print("usage: validate-combine-archive <OMEX File>")


def main(argv=None):
    args = argv if argv is not None else sys.argv[1:]
    if len(args) < 1:
        print_usage()
        return 1

    validate_omex_file(args[0])
    return 0

if __name__ == "__main__":
    sys.exit(main())