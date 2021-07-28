class chat:

    START_TEXT = "" Bu bot Filmle - Alt Dosyasını Yapıştırma / Birleştirme için mutlaka gerekir

<b> Başlamak için bana Film & Altyazı dosyası gönderir </b>

/help daha fazla ürün için..

    """

    HELP_USER = "??"

    HELP_TEXT ="""<b>Yardım Menüsüne Hoş Geldiniz</b>

1.) Bir Video dosyası veya url gönderin.
2.) Bir altyazı dosyası gönderin (ass veya srt)
3.) İstediğiniz muxing türünü seçin!

Dosyaya özel isim vermek için url'yi | ile ayrılmış olarak gönderin.
<i>url|özel_adı.mp4
</i>

<b>Not : </b><i>Hardmux'ta yalnızca ingilizce yazı tiplerinin desteklendiğini lütfen unutmayın, diğer komut dosyaları videoda boş bloklar olarak gösterilecektir!</i>

"""

    NO_AUTH_USER = "Bu botu kullanma yetkiniz yok.\nBot yiyesine iletişime geçin!"
    DOWNLOAD_SUCCESS = """Dosya başarıyla indirildi!

Geçen süre : {} saniye."""
    FILE_SIZE_ERROR = "HATA : URL'den Dosya Boyutu Çıkarılamıyor!"
    MAX_FILE_SIZE = "Dosya boyutu 2 Gb'den büyük. Telgraf tarafından belirlenen sınır budur!"
    LONG_CUS_FILENAME = """Sağladığınız dosya adı 60 karakterden uzun.
Lütfen daha kısa bir ad girin."""
    UNSUPPORTED_FORMAT = "HATA : Dosya biçimi {} Desteklenmiyor!"
