# Lab 02 — Feature/topic flow và Pull Request

## Vì sao đồng bộ `master` trước khi gửi PR?

Nhánh được tạo từ `master` cũ có thể thiếu thay đổi vừa hợp nhất. Đồng bộ bằng `git fetch` rồi `git merge origin/master` (hoặc rebase khi nhánh còn riêng) cho phép phát hiện xung đột và chạy lại test trên mã gần với trạng thái sẽ hợp nhất. Diff PR cũng dễ xem hơn, giúp reviewer đánh giá đúng thay đổi.

## Khi nào không được rebase?

Không rebase hoặc sửa lại lịch sử của nhánh chung khi người khác đã dựa trên các commit đó, đặc biệt là `master`, `release/*` hoặc nhánh đã chia sẻ mà không có thỏa thuận. Rebase tạo SHA mới; force push sau đó có thể làm mất hoặc gây trùng công việc của người khác. Với commit đã công bố cần hoàn tác, dùng `git revert`.

## `feature/*` khác `topic/*` ra sao?

`feature/*` dành cho hành vi/chức năng mới của sản phẩm (ví dụ `feature/search-by-title`). `topic/*` dành cho thay đổi theo một chủ đề khác như tài liệu, quy trình hoặc CI (`topic/pr-template`). Cả hai là nhánh sống ngắn, tạo từ `master`, qua PR rồi hợp nhất vào `master`; tên nhánh giúp người xem hiểu mục đích, không làm thay đổi cơ chế Git.

## Ba cách hợp nhất PR

`Merge commit` giữ các commit và điểm hội tụ. `Squash and merge` gộp thay đổi thành một commit mới, mất chi tiết commit trên nhánh. `Rebase and merge` tạo lại các commit với SHA mới trên đầu nhánh đích, cho lịch sử tuyến tính. Chọn theo nhu cầu truy vết và độ gọn của lịch sử; không dùng rebase để viết lại lịch sử nhánh đã chia sẻ.
