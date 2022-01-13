chrome.webRequest.onBeforeRequest.addListener(
    function(details) { 
      return {cancel: true}; 
    },
    {url: 
      ["*://*.doubleclick.net/*",]
    },
    ["blocking"]
  );
