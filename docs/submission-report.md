# Báo cáo tổng hợp bài thực hành IT3180

Repo này triển khai AIMS-mini theo [tài liệu thực hành Git và GitHub](https://drive.google.com/file/d/1RELVHF6fDGjb0pGkpbfFW7nHEe5FXbst/view). Các câu trả lời thảo luận được trình bày riêng để dễ đối chiếu:

| Bài | Báo cáo trả lời câu hỏi | Mốc bài nộp |
| --- | --- | --- |
| Lab 01 | [Thiết lập Git và refactor](answers-lab01.md) | `release/lab01`, `v0.1.0` |
| Lab 02 | [Feature/topic và Pull Request](answers-lab02.md) | `release/lab02`, `v0.2.0` |
| Lab 03 | [Bugfix, xung đột và hoàn tác](answers-lab03.md) | `release/lab03`, `v0.3.0` |
| Lab 04 | [Release và phiên bản](answers-lab04.md) | `release/lab04`, `v1.0.0` |
| Lab 05 | [Hotfix và bảo trì nhiều phiên bản](answers-lab05.md) | `release/lab04` tại `v1.0.1`; `release/lab05` tại `v1.1.0` |

## Kết quả kiểm tra

Ngày 24/10/2026, chạy `python3 main.py` từ bản lưu của từng tag và `master` đều thành công, cùng cho `Total cost: 63.89 $`. Chạy `python3 -m unittest discover -s tests -v` cho kết quả:

| Mốc | Số bài kiểm thử | Kết quả |
| --- | ---: | --- |
| `v0.1.0`, `v0.2.0` | Chưa có bộ kiểm thử | Ứng dụng chạy thành công |
| `v0.3.0`, `v1.0.0` | 6 | Đạt |
| `v1.0.1` | 7 | Đạt |
| `v1.1.0`, `master` | 9 | Đạt |

GitHub Actions cũng chạy thành công trên các Pull Request và lần đẩy `master` đã có workflow. [GitHub Release v1.0.0](https://github.com/nghunganh110/it3180-202416113-aims/releases/tag/v1.0.0) được phát hành từ tag của `release/lab04`. Các nhánh `master` và `release/lab01` đến `release/lab05` đã được cấu hình yêu cầu Pull Request; `master` còn yêu cầu kiểm thử `test` thành công. Khi làm một mình, số lượt phê duyệt bắt buộc là 0 theo hướng dẫn của bài.

## Phạm vi bằng chứng trên GitHub

Lịch sử Git có các nhánh refactor, feature, bugfix, release và hotfix, cùng commit sửa lỗi được cherry-pick. Tuy nhiên, các lần hợp nhất mã của những lab đầu được tạo trong lịch sử Git cục bộ trước khi đẩy lên GitHub. Vì vậy, lịch sử Pull Request trên GitHub không chứng minh được việc bạn cùng cặp review, vòng `Changes requested` → `Approved`, ba kiểu merge của Lab 02, hay Issue của những lỗi đã sửa ở Lab 03 và Lab 05. Không nên trình bày các bước đó như đã thực hiện trên GitHub.

Pull Request và Issue bổ sung báo cáo này thể hiện một vòng kiểm soát thay đổi thực tế. Nếu giảng viên yêu cầu bằng chứng review theo cặp cho từng lab, cần thực hiện thêm với một cộng tác viên thật.
