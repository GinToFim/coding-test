-- 코드를 입력하세요
SELECT board.title, board.board_id,
       reply.reply_id, reply.writer_id, reply.contents, 
       DATE_FORMAT(reply.created_date, "%Y-%m-%d") as created_date
  FROM used_goods_board AS board, used_goods_reply AS reply
 WHERE board.board_id = reply.board_id
   AND YEAR(board.created_date) = 2022
   AND MONTH(board.created_date) = 10
 ORDER BY created_date, title