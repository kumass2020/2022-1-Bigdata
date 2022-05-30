import asyncio

async function geocoding(url) {
    const req = await fetch(url);
    return req.json();
}
async function doGeocoding(address) {
    const result = await geocoding("http://api.vworld.kr/req/address?service=address"
        + "&request=getcoord"
        + "&address=" + encodeURI(address) + "&type=road"
        + "&key=838DDA11-A005-360D-8388-51D7EFC76EFC");
    console.log(result);
}
doGeocoding('서울시 성동구 아차산로7나길 18');
