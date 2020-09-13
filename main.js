var {google} = require('googleapis');

var service = google.youtube('v3')

service.videos.list({
    key:'AIzaSyBnTfkszuJqMF25idC4ud8jy_mWEOFR95M',
    part: 'snippet',
    id: 'qLrQBdJLodE',
    fields: 'items(snippet(title, description))'
},
function(err, res){
    if(err){
        console.log("This API doesn't work" + err)
        return
    }

    var video = res.data.items
    console.log(JSON.stringify(video, null, 4))
});