import csv


def write_to(target, header, mapper, mode="a", encode="utf-8"):
    """
    Write everything in the mapper to the given target directory,
    should be a csv file. Default encoding is utf-8, the should be
    a dict inside a dict, the format should be:
    {id1:{attribute:value, attribute:value...}, id2...}
    Arg: target: The target file location, in str
    Arg: header: The header that will be shown on the csv file
    Arg: mapper: The mapper, see above
    Arg: mode="a": Default mode is append
    Arg: encode="utf-8": Default encoding is utf-8\n
    The result of the csv file will look like:\n
    ===============HEADER======================
    \n
    id1 {
    attribute:value
    attribute:value
    }
    \n
    id2 {
    attribute:value
    attribute:value
    }
    ...
    """
    with open(target, mode, encoding=encode) as targ:
        writer = csv.writer(targ)
        # Write the header 
        writer.writerow(["=========="+header+"=========="])
        # Outer dict
        for outer_key in mapper:
            writer.writerow([outer_key+" {"])
            # Inner dict
            for inner_key in mapper[outer_key]:
                inner_dict = mapper[outer_key]
                writer.writerow([inner_key+":"+inner_dict[inner_key]])
            writer.writerow(["}"])
            writer.writerow("")
