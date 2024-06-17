// content.js

function extractText() {
    return document.body.innerText;
  }
  
  chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "extractText") {
      const pageText = extractText();
      sendResponse({ text: pageText });
    }
  });
  