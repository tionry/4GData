var express = require('express');
var app = express();
var fs = require('fs');
var server = http.createServer(app);

app.use(express.static('public'));
app.use(express.bodyParser({uploadDir:'./uploads'}));


app.get('/file-upload', function(req, res) {
 // 获得文件的临时路径
var tmp_path = req.files.thumbnail.path;
// 指定文件上传后的目录 - 示例为"images"目录。 
var target_path = './results/' + req.files.thumbnail.name;
// 移动文件
fs.rename(tmp_path, target_path, function(err) {
  if (err) throw err;
  // 删除临时文件夹文件, 
  fs.unlink(tmp_path, function() {
     if (err) throw err;
     res.send('File uploaded to: ' + target_path + ' - ' + req.files.thumbnail.size + ' bytes');
  });
});
});

var server = app.listen(80,function(){
	var host = server.address().address;
	var port = server.address().port
    console.log("监听地址为 http://%s:%s", host, port)
});