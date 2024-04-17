import os
import xml.etree.ElementTree as ET


def check_xml_for_object(xml_file):
    # 解析XML文件
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # 查找是否存在<object>标签
    object_tags = root.findall('.//object')

    # 如果不存在<object>标签，则返回False
    return len(object_tags) > 0


def main():
    # 设置图片文件夹和XML文件夹的路径
    image_folder = 'datasets/images'
    xml_folder = 'datasets/annotation/xmls'

    # 遍历XML文件夹中的文件
    for xml_file in os.listdir(xml_folder):
        if xml_file.endswith('.xml'):
            xml_path = os.path.join(xml_folder, xml_file)

            # 检查XML文件中是否存在<object>标签
            if not check_xml_for_object(xml_path):
                # 如果不存在<object>标签，则删除对应的jpg文件和xml文件
                image_file = os.path.join(image_folder, os.path.splitext(xml_file)[0] + '.jpg')
                if os.path.exists(image_file):
                    os.remove(image_file)
                os.remove(xml_path)
                print(f"Deleted {xml_file} and corresponding image file.")

    print("Done.")


if __name__ == "__main__":
    main()
