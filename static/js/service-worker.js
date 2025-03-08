self.addEventListener("install", function(event) {
    event.waitUntil(
        caches.open("static").then(function(cache) {
            return cache.addAll([
                "/",
                "/static/icons/icon-192x192.png",
                "/static/icons/icon-512x512.png"
            ]);
        })
    );
});

self.addEventListener("fetch", function(event) {
    event.respondWith(
        fetch(event.request).catch(() => caches.match(event.request))
    );
});