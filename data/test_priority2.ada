with Ada.Text_IO; use Ada.Text_IO;

procedure TestPrioriteOperateurs is
   function calculPriorite return integer is
      resultat: integer;
   begin
      resultat := 2 / 3 * 4;
      return resultat;
   end calculPriorite;

begin
   put(calculPriorite);
end TestPrioriteOperateurs;
