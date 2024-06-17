// popup.js

document.getElementById('readText').addEventListener('click', () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      chrome.tabs.sendMessage(tabs[0].id, { action: "extractText" }, (response) => {
        document.getElementById('textDisplay').innerText = response.text;
      });
    });
  });
  