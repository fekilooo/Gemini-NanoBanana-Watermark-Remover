// Listen for messages from content.js
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "fetchBlob") {
    fetch(request.url, {
      method: "GET",
      // Try to mimic a navigation request or identical origin request
      referrer: "https://gemini.google.com/",
      mode: "cors",
      credentials: "include" 
    })
      .then(response => {
        if (!response.ok) throw new Error(`Network response was not ok: ${response.status}`);
        return response.blob();
      })
      .then(blob => {
        // Convert Blob to Data URL (Base64) to send back to content script
        const reader = new FileReader();
        reader.onloadend = () => {
          sendResponse({ success: true, dataUrl: reader.result });
        };
        reader.onerror = () => {
          sendResponse({ success: false, error: 'Failed to read blob' });
        };
        reader.readAsDataURL(blob);
      })
      .catch(error => {
        sendResponse({ success: false, error: error.message });
      });
    return true; // Keep the message channel open for async response
  }
});