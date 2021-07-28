class Chat:

    START_TEXT = """ Salam , Bu bot videoya - Altyazı Dosyasını Birleştirme için tasarlanmış.

<b> Başlamak için bana Film & Altyazı dosyası gönderir </b>

/help daha çok bilgi için..

    """

    HELP_USER = "??"

    HELP_TEXT ="""<b>Yardım Menüsüne Hoş Geldiniz</b>

1.) Bir Video dosyası veya URL(bağlantı) gönderin.
2.) Altyazı dosyası gönderin (ass veya srt)
3.) İstediğiniz muxing türünü seçin! /softmux ya /hardmux

Dosyaya özel ad vermek için URL'yi | ile ayrılmış olarak gönderin.\n
<i><b> Örnek </b>: URL | özel_adı.mp4
</i>

"""

    NO_AUTH_USER = "Bu botu kullanma yetkiniz yok.\n Bot yiyesine iletişime geçin!"
    DOWNLOAD_SUCCESS = """Dosya başarıyla indirildi!

Geçen süre : {} saniye."""
    FILE_SIZE_ERROR = "HATA : URL'den Dosya Boyutu Çıkarılamıyor!"
    MAX_FILE_SIZE = "Dosya boyutu 2 Gb'den büyük. Telgraf tarafından belirlenen sınır budur!"
    LONG_CUS_FILENAME = """Sağladığınız dosya adı 60 karakterden uzun.
Lütfen daha kısa bir ad girin."""
    UNSUPPORTED_FORMAT = "HATA : Dosya biçimi {} Desteklenmiyor!"
