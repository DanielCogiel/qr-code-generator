import qrcode
import argparse
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', type=str, required=True, help='URL to generate QR code from.')
    parser.add_argument('-o', '--output', type=str, required=False, help='Output filename.')
    args = parser.parse_args()

    qr_code = qrcode.make(args.url)
    type(qr_code)

    output_folder_path = 'output'
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    qr_code.save(f"output/{args.output or 'qr-code'}.png")


if __name__ == '__main__':
    main()
