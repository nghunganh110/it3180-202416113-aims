# Lab 03 — Bugfix, xung đột và hoàn tác

## Merge base là gì?

Merge base là tổ tiên chung tốt nhất của hai commit hoặc hai nhánh. Git dùng nó làm bản gốc trong phép so sánh ba chiều: bản gốc, đầu nhánh của ta và đầu nhánh bên kia. Khi hai phía sửa cùng vùng kể từ merge base, Git có thể không tự quyết định được và báo xung đột. Dùng `git merge-base master feature/<tên>` để xem SHA; trường hợp lịch sử phức tạp có thể có nhiều merge base.

## Vì sao `master` và `release/*` phải dùng `revert`?

Hai nhánh này là lịch sử đã chia sẻ và là căn cứ kiểm toán. `reset` hoặc force push thay đổi hay bỏ các commit mà người khác đã lấy về, làm mất dấu vết và có thể phá các nhánh phụ thuộc. `git revert` tạo commit mới đảo ngược thay đổi, giữ nguyên lịch sử. Với merge commit, phải chọn parent chính, thường là `git revert -m 1 <sha>` khi muốn đảo phần được hợp nhất vào nhánh đích. Hoàn tác vẫn đi qua nhánh riêng và PR.

## Chứng cứ trong lịch sử repo

Nhánh `bugfix/cart-limit-off-by-one` ghi test lỗi trước khi sửa mã. Nhánh `bugfix/discount-calculation` bắt đầu từ `feature/discount`, với test và bản sửa trước khi tính năng vào `master`. Hai nhánh `feature/vietnamese-messages` và `feature/show-added-title` tạo xung đột thật trên cùng dòng; commit giải quyết giữ thông điệp tiếng Việt có tên DVD. Sau đó nhánh `bugfix/revert-show-added-title` đảo merge bằng `revert -m 1`.
