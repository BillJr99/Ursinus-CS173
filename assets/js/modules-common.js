/* Some common code shared throughout modules*/

var feedbackString = "";

const PROCESSING_CODE_BEGIN = `    
public static boolean drawn = false;
        void setup() {
            size(1, 1);
            noLoop();
        }
        void draw() {
            background(0);
            fill(255);
            stroke(255);`;

const PROCESSING_CODE_END = `
if (!drawn) {
    feedback.setValue(feedbackString);
    drawn = true;
}
}`;

function feedbackPrintln(s) {
    return s + "\n";
}

function feedbackPrint(s) {
    return s;
}

/**
 * Take code from the browser and put it into a form that can be sent to processing
 * 
 * @param {*} codeString All Java code (except for the main) that should be executed, as a string
 * @param {*} mainString A string of the Java code that should go in main
 * 
 * @return The final code that should be executed by processing.js
 */
function makeCodeJavaProcessing(codeString, mainString) {
    feedbackString = "";
    let str = codeString.replace(/System.out.print/g, "feedbackString += feedbackPrint");
    str += PROCESSING_CODE_BEGIN;
    str += mainString.replace(/System.out.print/g, "feedbackString += feedbackPrint");
    str += PROCESSING_CODE_END;
    // TODO: Hack for dealing with the fact that chars are cast to
    // ints in this transpiler
    str = str.replace(/'/g, "\"");
    console.log(str);
    return str;
}

/**
 * Convert the whitespace in a particular string to HTML whitespace
 * @param {string} s The input string
 */
function getHTMLWhitespace(s) {
    s = s.replace("\n", "<BR>");
    s = s.replace("\t", "&nbsp&nbsp&nbsp&nbsp");
    return s;
}

function removeTemplate(s) {
    while (s.indexOf("<Integer>") > -1) {
        s = s.replace("<Integer>", "");
    }
    while (s.indexOf("<String>") > -1) {
        s = s.replace("<String>", "");
    }
    while (s.indexOf("<String, Integer>") > -1) {
        s = s.replace("<String, Integer>", "");
    }
    while (s.indexOf("<Integer, Integer>") > -1) {
        s = s.replace("<Integer, Integer>", "");
    }
    while (s.indexOf("<>") > -1) {
        s = s.replace("<>", "");
    }
    return s;
}