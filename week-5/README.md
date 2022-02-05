● 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和
password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。
● 使用 SELECT 指令取得所有在 member 資料表中的會員資料。

INSERT INTO `member`(`name`,`username`, `password`, `follower_count`) values('new', 'new', 'new', 100);

![image](https://user-images.githubusercontent.com/95583422/152654387-a06de367-5e34-4f79-b922-b261e336d01c.png)

SELECT * FROM `member`;

![image](https://user-images.githubusercontent.com/95583422/152654397-e755124f-edd0-4269-b062-495fb6bbd6fe.png)


● 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由
近到遠排序。

SELECT * FROM `member` ORDER BY `time` DESC; 

![image](https://user-images.githubusercontent.com/95583422/152654404-5605d2dd-d242-4ab5-a9de-13ebd134ae42.png)

● 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，
由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )

SELECT * FROM `member` ORDER BY `time` DESC LIMIT 1, 3; 

![image](https://user-images.githubusercontent.com/95583422/152654428-83051cb8-b8ff-4d8c-a228-6e989f7a5de9.png)


● 使用 SELECT 指令取得欄位 username 是 test 的會員資料。

SELECT * FROM `member` WHERE `username` = 'test';

![image](https://user-images.githubusercontent.com/95583422/152654468-0d8f92ea-c9da-461d-aa8e-0c32acd9bc62.png)


● 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。

SELECT * FROM `member` WHERE `username` = 'test' AND `password` = 'test';

![image](https://user-images.githubusercontent.com/95583422/152654497-03bc4491-0e09-49ca-af60-3fe63a6a55cc.png)

● 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位
改成 test2。

UPDATE `member`
SET `username` = 'test2'
WHERE `username` = 'test';

![image](https://user-images.githubusercontent.com/95583422/152654523-1686f5d3-8c81-45f3-864b-fdc8aa0de09e.png)

SELECT * FROM `member`;

![image](https://user-images.githubusercontent.com/95583422/152654542-86655466-6196-4084-8916-37261b58c1e4.png)

● 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。

SELECT COUNT(*) FROM `member`;

![image](https://user-images.githubusercontent.com/95583422/152654562-e7dc7ccf-36fc-4c3b-9a48-445ad2a1dc25.png)

● 取得 member 資料表中，所有會員 follower_count 欄位的總和。

SELECT SUM(follower_count) FROM `member`;

![image](https://user-images.githubusercontent.com/95583422/152654593-c65a105a-afdd-4926-b44a-542991ccc51d.png)

● 取得 member 資料表中，所有會員 follower_count 欄位的平均數。

SELECT AVG(follower_count) FROM `member`;

![image](https://user-images.githubusercontent.com/95583422/152654608-55e48263-7920-4c05-be2d-7faf368153d1.png)

● 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。

SELECT `message`.*, `member`.`username`
FROM `message` INNER JOIN `member`
ON `message`.`member_id` = `member`.`id`;

![image](https://user-images.githubusercontent.com/95583422/152654653-64a90c1c-a715-493d-9970-cd981cab4afa.png)

● 使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有
留言，資料中須包含留言者會員的姓名。

SELECT `message`.*, `member`.`username`
FROM `message` INNER JOIN `member`
ON `message`.`member_id` = `member`.`id`
WHERE `member`.`username` = 'test';

![image](https://user-images.githubusercontent.com/95583422/152654672-4ddcf70a-3ea6-4b96-8fde-a73174335e58.png)
