var version = '0.2.3';
var _generate_css_names_from_string = function (item, split_on, prefix, suffix, midpoint) {
    if (prefix === void 0) { prefix = ''; }
    if (suffix === void 0) { suffix = ''; }
    if (midpoint === void 0) { midpoint = ''; }
    // https://stackoverflow.com/a/26156888
    var splitOnEscaped = split_on.replace(/[\-\[\]\/\{\}\(\)\*\+\?\.\\\^\$\|]/g, "\\$&");
    var toRemove = new RegExp("^${splitOnEscaped}+|{splitOnEscaped}+$", "g");
    var splitPath = item.replace(toRemove, "").split(split_on);
    // unquoted_path = (parse.unquote(item).strip() for item in split_path)
    var unquotedPath = [];
    for (var item_1 in splitPath) {
        unquotedPath.push(decodeURIComponent(item_1).trim());
    }
    // decoded_path = (codecs.decode(part.encode('utf-8'), "ascii", "ignore") for part in unquoted_path)
    var decodedPath = [];
    for (var part in unquotedPath) {
        // https://stackoverflow.com/a/20856346
        decodedPath.push(part.replace(/[^\x00-\x7F]/g, ""));
    }
    // escaped_path = (item for item in decoded_path if escape(item) == item)
    var escapedPath = [];
    for (var item_2 in decodedPath) {
        if (escape(item_2) === item_2) {
            escapedPath.push(item_2);
        }
    }
    // newpath = tuple(part for part in escaped_path if part)
    var newPath = [];
    for (var part in escapedPath) {
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
    var newpathLength = newPath.length + 1;
    // variations = (newpath[0:l] for l in range(1, newpath_length))
    var variations = [];
    for (var i = 1; i < newpathLength; i++) {
        variations.push(newPath.slice(0, i));
    }
    // if prefix and not prefix.endswith(('-', '_')):
    //     prefix = '%s%s' % (prefix, midpoint)
    var suffixes = ['-', '_'];
    var lastPrefixChar = prefix.substr(prefix.length - 1);
    if (prefix && (suffixes.indexOf(lastPrefixChar) === -1)) {
        prefix = "" + prefix + midpoint;
    }
    // if suffix and not suffix.startswith(('-', '_')):
    //     suffix = '%s%s' % (midpoint, suffix,)
    var firstSuffixChar = prefix.substr(0);
    if (suffix && (suffixes.indexOf(firstSuffixChar) === -1)) {
        suffix = "" + midpoint + suffix;
    }
    // finalised_variations = (
    //     '%s%s%s' % (prefix, midpoint.join(variation), suffix)
    //     for variation in variations
    // )
    var finalisedVariations = [];
    for (var variation in variations) {
        var finalVariation = '';
        finalisedVariations.push("" + prefix + finalVariation + suffix);
    }
    return finalisedVariations;
};
var path2css = function (path, prefix, suffix, midpoint, split_on) {
    if (prefix === void 0) { prefix = ''; }
    if (suffix === void 0) { suffix = ''; }
    if (midpoint === void 0) { midpoint = '-'; }
    if (split_on === void 0) { split_on = '/'; }
    var variations = _generate_css_names_from_string(path, split_on, prefix, suffix, midpoint);
    variations.toString = function () {
        return '????';
    };
};
