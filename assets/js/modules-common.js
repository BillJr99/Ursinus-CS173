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

function makeCode(codeString, mainString) {
    feedbackString = "";
    let str = codeString.replace(/System.out.print/g, "feedbackString += feedbackPrint");
    str += PROCESSING_CODE_BEGIN;
    str += mainString.replace(/System.out.print/g, "feedbackString += feedbackPrint");
    str += PROCESSING_CODE_END;
    return str;
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