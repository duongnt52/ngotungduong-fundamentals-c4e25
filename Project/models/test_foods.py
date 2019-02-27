#connect to database
import mlab
from mongoengine import Document, StringField , IntField

mlab.connect()

#define model (document)
class Nang(Document):
    ten = StringField()
    anh = StringField()
    diachi = StringField()
    nguyenlieu = StringField()
    cachlam = StringField()

class Lanh(Document):
    ten = StringField()
    anh = StringField()
    diachi = StringField()
    nguyenlieu = StringField()
    cachlam = StringField()

class Mat(Document):
    ten = StringField()
    anh = StringField()
    diachi = StringField()
    nguyenlieu = StringField()
    cachlam = StringField()

class Mua(Document):
    ten = StringField()
    anh = StringField()
    diachi = StringField()
    nguyenlieu = StringField()
    cachlam = StringField()


# create data

# n = Nang(ten = "Mỳ cay Samyang",
#         anh = "https://cdn.tgdd.vn/Files/2018/12/08/1136495/cach-nau-mi-cay-samyang-thom-ngon-kho-cuong-5_600x337.gif",
#         diachi = "50 Nguyễn Xiển, Quận Thanh Xuân, Hà Nội",
#         nguyenlieu = "1 gói mì cay Samyang, 1 cây xúc xích, 1 quả trứng gà, 1 muỗng cà phê tỏi băm, 1 muỗng canh dầu ăn, Hành lá",
#         cachlam = "Bóc gói mì ra. Mì gói trụng sơ qua nước sôi trong vòng 3-4 phút để mì nở rồi vớt ra. Cho tỏi băm vào chảo dầu nóng phi cho thơm rồi cho xúc xích vào xào sơ để xúc xích có mùi thơm và có màu đẹp mắt hơn. Cho mì và gói sốt cay vào trộn cho sợi mì thấm đều gia vị. Bắc 1 cái chảo khác và làm trứng ốp la. Cho mì và trứng ra dĩa, rắc lên một chút hành lá, mè rang và rong biển là xong."
#         )
# n.save()

# l = Lanh(ten = "Mỳ cay Samyang",
#         anh = "https://cdn.tgdd.vn/Files/2018/12/08/1136495/cach-nau-mi-cay-samyang-thom-ngon-kho-cuong-5_600x337.gif",
#         diachi = "50 Nguyễn Xiển, Quận Thanh Xuân, Hà Nội",
#         nguyenlieu = "1 gói mì cay Samyang, 1 cây xúc xích, 1 quả trứng gà, 1 muỗng cà phê tỏi băm, 1 muỗng canh dầu ăn, Hành lá",
#         cachlam = "Bóc gói mì ra. Mì gói trụng sơ qua nước sôi trong vòng 3-4 phút để mì nở rồi vớt ra. Cho tỏi băm vào chảo dầu nóng phi cho thơm rồi cho xúc xích vào xào sơ để xúc xích có mùi thơm và có màu đẹp mắt hơn. Cho mì và gói sốt cay vào trộn cho sợi mì thấm đều gia vị. Bắc 1 cái chảo khác và làm trứng ốp la. Cho mì và trứng ra dĩa, rắc lên một chút hành lá, mè rang và rong biển là xong."
#         )
# l.save()


# m = Mat(ten = "Cháo Sườn",
#         anh = "https://images.foody.vn/res/g20/194137/prof/s640x400/foody-mobile-5-jpg-507-635853442751633602.jpg",
#         diachi = "45 Cửa Bắc, Ba Đình , Hà Nội",
#         nguyenlieu = "150 grm bột gạo tẻ, 2 thìa bột gạo nếp, 3-400 grm sườn sụn (sườn non), 2 củ hành tím, 3 cái quẩy to",
#         cachlam = "Sườn sụn rửa sạch, đổ vào khoảng 2 bát to nước, đun trong nồi áp suất khoảng 10-15' (sườn có độ chín vừa phải, ăn vẫn sần sật) Nếu bạn nào thích mềm hẳn thì đun thêm nhá. Vớt sườn ra để nguội rồi thái mỏng thành miếng vừa ăn. Nhớ giữ lại nước sườn nhé. Hành khô thái nhỏ, phi thơm rồi cho sườn vào đảo cùng. Nêm vừa ăn.(mình chỉ cho bột nêm, ko cho nc mắm vì sợ lúc bỏ vào cháo sẽ có mùi nước măm). Bột gạo hoà với 1 chút nước, đổ vào nồi (tốt nhất là dùng nồi chống dính nhá). Vừa đun vừa đổ dần nước dùng ninh sườn vào, khuấy đều tránh vón cục. Khi bột đã tan hết, chuyển thành trong thì cho sườn vào, giảm nhỏ lửa, đun thêm 15-20p. Nêm gia vị vừa miệng. Múc ra bát tô, cắt quẩy, rắc hạt tiêu rồi chén thôi."
#         )
# m.save()

# r = Mua(ten = "Ốc luộc",
#         anh = "https://daubepgiadinh.vn/wp-content/uploads/2017/07/cach-luoc-oc-ngon.jpg",
#         diachi = "2B Đặng Văn Ngữ, Quận Đống Đa, Hà Nội",
#         nguyenlieu = " 2kg ốc, 10 lá bưởi/ chanh, 5 củ sả, 2 quả ớt (nếu thích ăn cay có thể cho hơn), Nước chấm: sả, gừng, tỏi, ớt, mắm, lá chanh ",
#         cachlam = "Làm sạch ốc. \nỐc sau khi rửa sạch, cho vào nồi, bỏ thêm lá bưởi (hoặc lá chanh), vài cọng sả, một chút xíu nước. Bản thân ốc đã chứa nhiều nước nên dù không cho thêm cũng không sợ cháy nồi. Đậy vung, đặt nồi lên bếp đun đều lửa. Khi ốc sôi trào, lập tức mở vung, đảo lên một lượt, thấy vẩy bong đều là được. Thường ốc chín sau khi sôi khoảng 2 - 3 phút. Không nên đun lâu quá kẻo ruột ốc thụt vào trong và đứt đoạn, rất khó khêu; Cách pha nước chấm: Nước mắm ngon + nước sôi để nguội + đường trộn đều bắc lên bếp đun sôi cho tan đường để nguội. Sau đó cho gừng + tỏi + ớt bằm nhuyễn + nước cốt chanh vào trộn đều. Rắc xả thái nhỏ lên trên và trộn đều. Nếu thích ăn cay, bạn nên cho ớt cay hoặc ớt nghiền vào sẽ ngon hơn nhiều. "
#         )
# r.save()