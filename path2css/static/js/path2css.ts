const version = '0.2.3';

const _generate_css_names_from_string = (item: string, split_on: string, prefix='', suffix='', midpoint='') => {
    // https://stackoverflow.com/a/26156888
    const splitOnEscaped = split_on.replace(/[\-\[\]\/\{\}\(\)\*\+\?\.\\\^\$\|]/g, "\\$&");
    const toRemove = new RegExp(`^\${splitOnEscaped}+|\{splitOnEscaped}+$`, "g");
    const splitPath = item.replace(toRemove, "").split(split_on)
    // unquoted_path = (parse.unquote(item).strip() for item in split_path)
    const unquotedPath: string[] = [];
    for (const item in splitPath) {
        unquotedPath.push(decodeURIComponent(item).trim())
    }
    // decoded_path = (codecs.decode(part.encode('utf-8'), "ascii", "ignore") for part in unquoted_path)
    const decodedPath: string[] = [];
    for (const part in unquotedPath) {
        // https://stackoverflow.com/a/20856346
        decodedPath.push(part.replace(/[^\x00-\x7F]/g, ""));
    }
    // escaped_path = (item for item in decoded_path if escape(item) == item)
    const escapedPath: string[] = [];
    for (const item in decodedPath) {
        if (escape(item) === item) {
            escapedPath.push(item)
        }
    }
    // newpath = tuple(part for part in escaped_path if part)
    const newPath: string[] = [];
    for (const part in escapedPath) {
        if (part.trim()) {
            newPath.push(part.trim());
        }
    }
    // if not newpath:
    //     return ()
    if (newPath.length === 0) {
        return [];
    }
    // newpath_length = len(newpath) + 1
    const newpathLength = newPath.length + 1;

    // variations = (newpath[0:l] for l in range(1, newpath_length))
    const variations: string[][] = [];
    for (let i = 1; i < newpathLength; i++) {
        variations.push(newPath.slice(0, i));
    }

    // if prefix and not prefix.endswith(('-', '_')):
    //     prefix = '%s%s' % (prefix, midpoint)
    const suffixes = ['-', '_'];
    const lastPrefixChar = prefix.substr(prefix.length - 1);
    if (prefix && (suffixes.indexOf(lastPrefixChar) === -1)) {
        prefix = `${prefix}${midpoint}`
    }
    // if suffix and not suffix.startswith(('-', '_')):
    //     suffix = '%s%s' % (midpoint, suffix,)
    const firstSuffixChar = prefix.substr(0);
    if (suffix && (suffixes.indexOf(firstSuffixChar) === -1)) {
        suffix = `${midpoint}${suffix}`
    }
    // finalised_variations = (
    //     '%s%s%s' % (prefix, midpoint.join(variation), suffix)
    //     for variation in variations
    // )
    const finalisedVariations: string[] = [];
    for (const variation in variations) {
        const finalVariation = '';
        finalisedVariations.push(
            `${prefix}${finalVariation}${suffix}`
        )
    }
    return finalisedVariations;
}

const path2css = (path: string, prefix='', suffix='', midpoint='-', split_on='/') => {
    const variations = _generate_css_names_from_string(path, split_on, prefix, suffix, midpoint);
    variations.toString = () => {
        return '????'
    }
}
