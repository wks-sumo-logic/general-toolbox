import tsFileStruct = require("ts-file-parser")
var filePath = "<SampleTSFile>.ts";
var decls = fs.readFileSync(filePath).toString();
var jsonStructure = tsFileStruct.parseStruct(decls, {}, filePath);
